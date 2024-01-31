import functools
from typing import Any, Callable, Dict, List, Optional, Tuple, get_origin

from classiq.interface.executor.execution_preferences import ExecutionPreferences
from classiq.interface.generator.model.constraints import Constraints
from classiq.interface.generator.model.preferences.preferences import Preferences
from classiq.interface.model.model import Model, SerializedModel
from classiq.interface.model.native_function_definition import NativeFunctionDefinition
from classiq.interface.model.quantum_function_declaration import (
    QuantumFunctionDeclaration,
)

from classiq.exceptions import ClassiqError
from classiq.qmod.declaration_inferrer import infer_func_decl
from classiq.qmod.qmod_parameter import QParam
from classiq.qmod.qmod_variable import QVar
from classiq.qmod.quantum_callable import QCallable
from classiq.qmod.quantum_expandable import QExpandable, QTerminalCallable
from classiq.qmod.utilities import mangle_keyword, unmangle_keyword


def _lookup_qfunc(name: str) -> Optional[QuantumFunctionDeclaration]:
    # FIXME: to be generalized to existing user-defined functions
    return QuantumFunctionDeclaration.BUILTIN_FUNCTION_DECLARATIONS.get(name)


def create_model(
    entry_point: "QFunc",
    constraints: Optional[Constraints] = None,
    execution_preferences: Optional[ExecutionPreferences] = None,
    preferences: Optional[Preferences] = None,
) -> SerializedModel:
    return entry_point.create_model(
        constraints, execution_preferences, preferences
    ).get_model()


class QFunc(QExpandable):
    def __init__(self, py_callable: Callable) -> None:
        _validate_no_gen_params(py_callable.__annotations__)
        super().__init__(py_callable)
        functools.update_wrapper(self, py_callable)

    @property
    def func_decl(self) -> QuantumFunctionDeclaration:
        return self._qmodule.native_defs.get(
            self._py_callable.__name__,
            infer_func_decl(self._py_callable, qmodule=self._qmodule),
        )

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        super().__call__(*args, **kwargs)
        self._add_native_func_def()

    def create_model(
        self,
        constraints: Optional[Constraints] = None,
        execution_preferences: Optional[ExecutionPreferences] = None,
        preferences: Optional[Preferences] = None,
    ) -> Model:
        self._qmodule.type_decls = dict()
        self._qmodule.native_defs = dict()
        self._add_native_func_def()
        model_extra_settings: List[Tuple[str, Any]] = [
            ("constraints", constraints),
            ("execution_preferences", execution_preferences),
            ("preferences", preferences),
        ]
        return Model(
            functions=list(self._qmodule.native_defs.values()),
            types=list(self._qmodule.type_decls.values()),
            **{key: value for key, value in model_extra_settings if value},
        )

    def _add_native_func_def(self) -> None:
        if self.func_decl.name in self._qmodule.native_defs:
            return
        self.expand()
        self._qmodule.native_defs[self.func_decl.name] = NativeFunctionDefinition(
            **self.func_decl.__dict__, body=self.body
        )


class ExternalQFunc(QTerminalCallable):
    def __init__(self, py_callable: Callable) -> None:
        decl = _lookup_qfunc(unmangle_keyword(py_callable.__name__))
        if decl is None:
            raise ValueError(f"Definition of {py_callable.__name__!r} not found")

        py_callable.__annotations__.pop("return", None)
        if py_callable.__annotations__.keys() != {
            mangle_keyword(arg.name) for arg in decl.get_positional_arg_decls()
        }:
            raise ValueError(
                f"Parameter type hints for {py_callable.__name__!r} do not match imported declaration"
            )
        super().__init__(decl)
        functools.update_wrapper(self, py_callable)


ILLEGAL_PARAM_ERROR = "Unsupported type hint '{annotation}' for argument '{name}'."


class IllegalParamsError(ClassiqError):
    _HINT = "\nNote - QMOD functions can declare classical parameters using the type hint 'QParam'."

    def __init__(self, message: str) -> None:
        super().__init__(message + self._HINT)


def _validate_no_gen_params(annotations: Dict[str, Any]) -> None:
    _illegal_params = {
        name: annotation
        for name, annotation in annotations.items()
        if not (
            name == "return"
            or get_origin(annotation) is QParam
            or (get_origin(annotation) or annotation) is QCallable
            or QVar.from_type_hint(annotation) is not None
        )
    }
    if _illegal_params:
        raise IllegalParamsError(
            "\n".join(
                ILLEGAL_PARAM_ERROR.format(name=name, annotation=annotation)
                for name, annotation in _illegal_params.items()
            )
        )
