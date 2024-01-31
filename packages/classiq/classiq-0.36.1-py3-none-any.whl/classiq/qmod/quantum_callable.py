import sys
from abc import ABC, abstractmethod
from typing import _GenericAlias  # type: ignore[attr-defined]
from typing import Any, ClassVar, Generic, Optional

from typing_extensions import ParamSpec

from classiq.interface.model.quantum_function_call import QuantumFunctionCall
from classiq.interface.model.quantum_function_declaration import (
    QuantumFunctionDeclaration,
)
from classiq.interface.model.quantum_statement import QuantumStatement
from classiq.interface.model.quantum_type import QuantumType

P = ParamSpec("P")


class QExpandableInterface(ABC):
    @abstractmethod
    def append_statement_to_body(self, stmt: QuantumStatement) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_local_handle(self, name: str, qtype: QuantumType) -> None:
        raise NotImplementedError()


class QCallable(Generic[P]):
    CURRENT_EXPANDABLE: ClassVar[Optional[QExpandableInterface]] = None

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        assert QCallable.CURRENT_EXPANDABLE is not None
        QCallable.CURRENT_EXPANDABLE.append_statement_to_body(
            self.create_quantum_function_call(*args, **kwargs)
        )
        return

    @property
    @abstractmethod
    def func_decl(self) -> QuantumFunctionDeclaration:
        raise NotImplementedError

    # Support comma-separated generic args in older Python versions
    if sys.version_info[0:2] < (3, 10):

        def __class_getitem__(cls, args) -> _GenericAlias:
            return _GenericAlias(cls, args)

    @abstractmethod
    def create_quantum_function_call(
        self, *args: Any, **kwargs: Any
    ) -> QuantumFunctionCall:
        raise NotImplementedError()
