from typing import Any, Dict, Optional

from classiq.interface.generator.control_state import ControlState


class OperatorSynthesisData:
    @property
    def call_kwargs(self) -> Dict[str, Any]:
        return dict()


class PowerOperatorSynthesisData(OperatorSynthesisData):
    def __init__(self, power: int) -> None:
        self._power = power

    @property
    def call_kwargs(self) -> Dict[str, Any]:
        return {"power": self._power}


class InvertOperatorSynthesisData(OperatorSynthesisData):
    @property
    def call_kwargs(self) -> Dict[str, Any]:
        return {"is_inverse": True}


class ControlOperatorSynthesisData(OperatorSynthesisData):
    _CTRL_VAR_NAME = "ctrl"

    def __init__(self, ctrl_size: int, ctrl_state: Optional[str] = None) -> None:
        ctrl_state_kwargs = dict()
        if ctrl_state is not None:
            ctrl_state_kwargs["ctrl_state"] = ctrl_state
        self._ctrl_state = ControlState(
            name=self._CTRL_VAR_NAME, num_ctrl_qubits=ctrl_size, **ctrl_state_kwargs
        )

    @property
    def call_kwargs(self) -> Dict[str, Any]:
        return {
            "control_states": [self._ctrl_state],
        }


class ComputeOperatorSynthesisData(OperatorSynthesisData):
    @property
    def call_kwargs(self) -> Dict[str, Any]:
        return {"should_control": False}
