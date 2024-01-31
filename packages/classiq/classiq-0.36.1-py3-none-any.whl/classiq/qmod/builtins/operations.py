from typing import Callable, List, Union

from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.model.bind_operation import BindOperation
from classiq.interface.model.inplace_binary_operation import (
    BinaryOperation,
    InplaceBinaryOperation,
)
from classiq.interface.model.numeric_reinterpretation import (
    NumericReinterpretationOperation,
)

from classiq.exceptions import ClassiqValueError
from classiq.qmod.builtins.functions import (
    apply,
    compute as compute_operator,
    control_with_value,
    uncompute,
)
from classiq.qmod.qmod_parameter import QParam
from classiq.qmod.qmod_variable import Input, Output, QNum, QVar
from classiq.qmod.quantum_callable import QCallable
from classiq.qmod.symbolic_expr import SymbolicEquality, SymbolicExpr


def bind(source: Input[QVar], destination: Output[QVar]) -> None:
    assert QCallable.CURRENT_EXPANDABLE is not None
    QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
        BindOperation(
            in_handle=source.get_handle_binding(),
            out_handle=destination.get_handle_binding(),
        )
    )


QUANTUM_IF_CONDITION_ARG_ERROR_MESSAGE_PREFIX = (
    "quantum_if condition must be of the form '<quantum-variable> == "
    "<classical-integer-expression>', but "
)


def quantum_if(
    condition: SymbolicExpr, then: Union[QCallable, Callable[[], None]]
) -> None:
    if not isinstance(condition, SymbolicEquality):
        raise ClassiqValueError(
            f"quantum_if condition must be an equality, was " f"{condition!r}"
        )
    ctrl, ctrl_val = condition.lhs, condition.rhs
    if isinstance(ctrl, (int, SymbolicExpr)) and isinstance(ctrl_val, QNum):
        ctrl, ctrl_val = ctrl_val, ctrl

    if not isinstance(ctrl, QNum):
        raise ClassiqValueError(
            QUANTUM_IF_CONDITION_ARG_ERROR_MESSAGE_PREFIX
            + f"condition's left-hand side was {ctrl!r} of type "
            f"{type(ctrl)}"
        )
    if not isinstance(ctrl_val, (int, SymbolicExpr)):
        raise ClassiqValueError(
            QUANTUM_IF_CONDITION_ARG_ERROR_MESSAGE_PREFIX
            + f"condition's right-hand side was {ctrl_val!r} of type "
            f"{type(ctrl_val)}"
        )
    control_with_value(ctrl_val, then, ctrl)


def reinterpret_num(
    is_signed: Union[QParam[bool], bool],
    fraction_digits: Union[QParam[int], int],
    target: QNum,
) -> None:
    assert QCallable.CURRENT_EXPANDABLE is not None
    QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
        NumericReinterpretationOperation(
            target=target.get_handle_binding(),
            is_signed=Expression(expr=str(is_signed)),
            fraction_digits=Expression(expr=str(fraction_digits)),
        )
    )


def inplace_add(
    value: QNum,
    target: QNum,
) -> None:
    assert QCallable.CURRENT_EXPANDABLE is not None
    QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
        InplaceBinaryOperation(
            target=target.get_handle_binding(),
            value=value.get_handle_binding(),
            operation=BinaryOperation.Addition,
        )
    )


def inplace_xor(
    value: QNum,
    target: QNum,
) -> None:
    assert QCallable.CURRENT_EXPANDABLE is not None
    QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
        InplaceBinaryOperation(
            target=target.get_handle_binding(),
            value=value.get_handle_binding(),
            operation=BinaryOperation.Xor,
        )
    )


def within_apply(
    compute: Callable[[], None],
    action: Callable[[], None],
) -> None:
    compute_operator(compute)
    apply(action)
    uncompute(compute)


__all__ = [
    "bind",
    "quantum_if",
    "reinterpret_num",
    "inplace_add",
    "inplace_xor",
    "within_apply",
]


def __dir__() -> List[str]:
    return __all__
