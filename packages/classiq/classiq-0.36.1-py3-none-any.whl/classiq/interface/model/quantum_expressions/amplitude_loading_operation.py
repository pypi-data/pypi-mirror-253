from typing import Dict, Mapping, Union

import pydantic

from classiq.interface.generator.amplitude_loading import (
    AMPLITUDE_IO_NAME,
    TARGET_OUTPUT_NAME,
)
from classiq.interface.model.handle_binding import (
    HandleBinding,
    SlicedHandleBinding,
    SubscriptHandleBinding,
)
from classiq.interface.model.quantum_expressions.quantum_expression import (
    QuantumExpressionOperation,
)
from classiq.interface.model.quantum_type import QuantumBit, QuantumNumeric, QuantumType

from classiq.exceptions import ClassiqValueError

MULTI_VARS_UNSUPPORTED_ERROR = (
    "Amplitude Loading with more than one input variable is unsupported."
)

VAR_DOMAIN_ILLEGAL = (
    "Amplitude Loading input variable should be a fixed-point number between 0 and 1"
)


class AmplitudeLoadingOperation(QuantumExpressionOperation):
    _result_type: QuantumType = pydantic.PrivateAttr(default_factory=QuantumBit)

    @property
    def wiring_inouts(
        self,
    ) -> Mapping[
        str, Union[SlicedHandleBinding, SubscriptHandleBinding, HandleBinding]
    ]:
        if len(self.var_handles) == 0:
            return dict()
        return {AMPLITUDE_IO_NAME: self.var_handles[0]}

    def initialize_var_types(
        self,
        var_types: Dict[str, QuantumType],
        machine_precision: int,
    ) -> None:
        if len(var_types) != 1:
            raise ClassiqValueError(MULTI_VARS_UNSUPPORTED_ERROR)
        var_type = var_types[self.var_handles[0].name]
        if not (
            isinstance(var_type, QuantumNumeric)
            and var_type.fraction_digits == var_type.size_in_bits
        ):
            raise ClassiqValueError(VAR_DOMAIN_ILLEGAL)
        super().initialize_var_types(var_types, machine_precision)

    @classmethod
    def result_name(cls) -> str:
        return TARGET_OUTPUT_NAME
