from typing import Mapping

import pydantic

from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.model.handle_binding import HandleBinding
from classiq.interface.model.quantum_statement import QuantumOperation

from classiq.exceptions import ClassiqValueError


class NumericReinterpretationOperation(QuantumOperation):
    target: HandleBinding
    fraction_digits: Expression
    is_signed: Expression

    @property
    def wiring_inouts(self) -> Mapping[str, HandleBinding]:
        return {"target": self.target}

    @pydantic.validator("target")
    def validate_handle(cls, handle: HandleBinding) -> HandleBinding:
        if not handle.is_bindable():
            raise ClassiqValueError(f"Cannot bind '{handle}'")  # noqa: B907
        return handle
