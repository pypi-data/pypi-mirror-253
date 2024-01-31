from abc import ABC
from types import TracebackType
from typing import Any, Callable, ClassVar, Dict, List, Optional, Type, Union

from typing_extensions import Self

from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.model.classical_parameter_declaration import (
    ClassicalParameterDeclaration,
)
from classiq.interface.model.port_declaration import PortDeclaration
from classiq.interface.model.quantum_function_call import (
    ArgValue,
    QuantumFunctionCall,
    QuantumLambdaFunction,
)
from classiq.interface.model.quantum_function_declaration import (
    PositionalArg,
    QuantumFunctionDeclaration,
    QuantumOperandDeclaration,
)
from classiq.interface.model.quantum_statement import QuantumStatement
from classiq.interface.model.quantum_type import QuantumType
from classiq.interface.model.variable_declaration_statement import (
    VariableDeclarationStatement,
)

from classiq.exceptions import ClassiqValueError
from classiq.qmod.model_state_container import QMODULE, ModelStateContainer
from classiq.qmod.qmod_parameter import QParam, create_param
from classiq.qmod.qmod_variable import QVar, create_qvar_for_port_decl
from classiq.qmod.quantum_callable import QCallable, QExpandableInterface
from classiq.qmod.utilities import mangle_keyword

ArgType = Union[QParam, QVar, QCallable]


class QExpandable(QCallable, QExpandableInterface, ABC):
    STACK: ClassVar[List["QExpandable"]] = list()

    def __init__(self, py_callable: Callable) -> None:
        self._qmodule: ModelStateContainer = QMODULE
        self._py_callable: Callable = py_callable
        self._body: List[QuantumStatement] = list()

    @property
    def body(self) -> List[QuantumStatement]:
        return self._body

    def __enter__(self) -> Self:
        QExpandable.STACK.append(self)
        QCallable.CURRENT_EXPANDABLE = self
        self._body.clear()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        assert QExpandable.STACK.pop() is self
        QCallable.CURRENT_EXPANDABLE = (
            QExpandable.STACK[-1] if QExpandable.STACK else None
        )

    def expand(self) -> None:
        with self:
            self._py_callable(*self._get_positional_args())

    def infer_rename_params(self) -> Dict[str, str]:
        return {}

    def add_local_handle(self, name: str, qtype: QuantumType) -> None:
        self._body.append(VariableDeclarationStatement(name=name, quantum_type=qtype))

    def append_statement_to_body(self, stmt: QuantumStatement) -> None:
        self._body.append(stmt)

    def _get_positional_args(self) -> List[ArgType]:
        result: List[ArgType] = []
        for arg in self.func_decl.get_positional_arg_decls():
            if isinstance(arg, ClassicalParameterDeclaration):
                rename_dict = self.infer_rename_params()
                actual_name = (
                    rename_dict[arg.name] if arg.name in rename_dict else arg.name
                )
                result.append(
                    create_param(actual_name, arg.classical_type, self._qmodule)
                )
            elif isinstance(arg, PortDeclaration):
                result.append(create_qvar_for_port_decl(arg))
            else:
                assert isinstance(arg, QuantumOperandDeclaration)
                result.append(QTerminalCallable(arg))
        return result

    def create_quantum_function_call(
        self, *args: Any, **kwargs: Any
    ) -> QuantumFunctionCall:
        return _create_quantum_function_call(self.func_decl, *args, **kwargs)


class QLambdaFunction(QExpandable):
    def __init__(self, decl: QuantumFunctionDeclaration, py_callable: Callable) -> None:
        py_callable.__annotations__.pop("return", None)
        super().__init__(py_callable)
        self._decl = decl

    @property
    def func_decl(self) -> QuantumFunctionDeclaration:
        return self._decl

    def infer_rename_params(self) -> Dict[str, str]:
        if not self._py_callable.__annotations__:
            return {}
        return {
            decl_name: actual_name
            for decl_name, actual_name in list(
                zip(
                    [arg.name for arg in self.func_decl.get_positional_arg_decls()],
                    self._py_callable.__annotations__.keys(),
                )
            )
            if decl_name != actual_name
        }


class QTerminalCallable(QCallable):
    def __init__(self, decl: QuantumFunctionDeclaration) -> None:
        self._decl = decl

    @property
    def func_decl(self) -> QuantumFunctionDeclaration:
        return self._decl

    def create_quantum_function_call(
        self, *args: Any, **kwargs: Any
    ) -> QuantumFunctionCall:
        return _create_quantum_function_call(self.func_decl, *args, **kwargs)


def _prepare_arg(arg_decl: PositionalArg, val: Any) -> ArgValue:
    if isinstance(arg_decl, ClassicalParameterDeclaration):
        return Expression(expr=str(val))
    elif isinstance(arg_decl, PortDeclaration):
        return val.get_handle_binding()
    else:
        if not isinstance(val, QCallable):
            val = QLambdaFunction(arg_decl, val)

        if not isinstance(val, QExpandable):
            return val.func_decl.name

        val.expand()
        return QuantumLambdaFunction(
            rename_params=val.infer_rename_params(), body=val.body
        )


def _get_operand_hint_args(
    func: QuantumFunctionDeclaration, param: PositionalArg, param_value: str
) -> str:
    return ", ".join(
        [
            f"{decl.name}={param_value}"
            if decl.name == param.name
            else f"{decl.name}=..."
            for decl in func.get_positional_arg_decls()
        ]
    )


def _get_operand_hint(func: QuantumFunctionDeclaration, param: PositionalArg) -> str:
    return (
        f"\nHint: To create an operand, do not call quantum gates directly "
        f"`{func.name}({_get_operand_hint_args(func, param, 'H(q)')})`. "
        f"Instead, use a lambda function "
        f"`{func.name}({_get_operand_hint_args(func, param, 'lambda: H(q)')})` "
        f"or a quantum function "
        f"`{func.name}({_get_operand_hint_args(func, param, 'my_func')})`"
    )


def _prepare_args(
    decl: QuantumFunctionDeclaration, arg_list: List[Any], kwargs: Dict[str, Any]
) -> List[ArgValue]:
    result = []
    for arg_decl in decl.get_positional_arg_decls():
        if arg_list:
            arg = arg_list.pop(0)
        else:
            arg = kwargs.pop(mangle_keyword(arg_decl.name), None)
        if arg is None:
            error_message = (
                f"{decl.name!r} is missing required argument for {arg_decl.name!r}"
            )
            if isinstance(arg_decl, QuantumOperandDeclaration):
                error_message += _get_operand_hint(decl, arg_decl)
            raise ClassiqValueError(error_message)
        result.append(_prepare_arg(arg_decl, arg))

    return result


def _create_quantum_function_call(
    decl: QuantumFunctionDeclaration, *args: Any, **kwargs: Any
) -> QuantumFunctionCall:
    arg_decls = decl.get_positional_arg_decls()
    arg_list = list(args)
    prepared_args = _prepare_args(decl, arg_list, kwargs)

    if kwargs:
        bad_kwarg = next(iter(kwargs))
        if not all(arg_decl.name == bad_kwarg for arg_decl in arg_decls):
            raise ClassiqValueError(
                f"{decl.name}() got an unexpected keyword argument {bad_kwarg!r}"
            )
        else:
            raise ClassiqValueError(
                f"{decl.name}() got multiple values for argument {bad_kwarg!r}"
            )
    if arg_list:
        raise ClassiqValueError(
            f"{decl.name}() takes {len(arg_decls)} arguments but {len(args)} were given"
        )

    return QuantumFunctionCall(function=decl.name, positional_args=prepared_args)
