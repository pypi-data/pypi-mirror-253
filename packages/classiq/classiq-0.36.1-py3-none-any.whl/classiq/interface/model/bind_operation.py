from typing import Mapping

import pydantic

from classiq.interface.model.handle_binding import HandleBinding
from classiq.interface.model.quantum_statement import QuantumOperation

from classiq.exceptions import ClassiqValueError

BIND_INPUT_NAME = "bind_input"
BIND_OUTPUT_NAME = "bind_output"


class BindOperation(QuantumOperation):
    in_handle: HandleBinding
    out_handle: HandleBinding

    @property
    def wiring_inputs(self) -> Mapping[str, HandleBinding]:
        return {BIND_INPUT_NAME: self.in_handle}

    @property
    def wiring_outputs(self) -> Mapping[str, HandleBinding]:
        return {BIND_OUTPUT_NAME: self.out_handle}

    @pydantic.validator("in_handle", "out_handle")
    def validate_handle(cls, handle: HandleBinding) -> HandleBinding:
        if not handle.is_bindable():
            raise ClassiqValueError(f"Cannot bind '{handle}'")  # noqa: B907
        return handle
