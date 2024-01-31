import abc
import ast
from typing import Dict, List, Mapping, Optional, Set, Union

import pydantic

from classiq.interface.generator.arith.arithmetic_expression_validator import (
    DEFAULT_SUPPORTED_FUNC_NAMES,
)
from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.expressions.sympy_supported_expressions import (
    SYMPY_SUPPORTED_EXPRESSIONS,
)
from classiq.interface.helpers.pydantic_model_helpers import nameables_to_dict
from classiq.interface.model.handle_binding import (
    HandleBinding,
    SlicedHandleBinding,
    SubscriptHandleBinding,
)
from classiq.interface.model.quantum_statement import QuantumOperation
from classiq.interface.model.quantum_type import QuantumType


class VarRefCollector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.var_names: Set[str] = set()

    def generic_visit(self, node: ast.AST) -> None:
        if isinstance(node, ast.Name) and node.id not in set(
            SYMPY_SUPPORTED_EXPRESSIONS
        ) | set(DEFAULT_SUPPORTED_FUNC_NAMES):
            self.var_names.add(node.id)
        super().generic_visit(node)


class QuantumExpressionOperation(QuantumOperation):
    expression: Expression = pydantic.Field()
    result_var: HandleBinding = pydantic.Field(
        description="The variable storing the expression result"
    )
    _var_handles: List[HandleBinding] = pydantic.PrivateAttr(
        default_factory=list,
    )
    _var_types: Dict[str, QuantumType] = pydantic.PrivateAttr(
        default_factory=dict,
    )
    _result_type: Optional[QuantumType] = pydantic.PrivateAttr(
        default=None,
    )

    @property
    def var_handles(self) -> List[HandleBinding]:
        return self._var_handles

    def set_var_handles(self, var_handles: List[HandleBinding]) -> None:
        self._var_handles = var_handles

    @property
    def var_types(self) -> Dict[str, QuantumType]:
        return self._var_types

    def initialize_var_types(
        self,
        var_types: Dict[str, QuantumType],
        machine_precision: int,
    ) -> None:
        assert len(var_types) == len(self.var_handles)
        self._var_types = var_types

    @property
    def wiring_inouts(
        self,
    ) -> Mapping[
        str, Union[SlicedHandleBinding, SubscriptHandleBinding, HandleBinding]
    ]:
        return nameables_to_dict(self.var_handles)

    @property
    def wiring_outputs(self) -> Mapping[str, HandleBinding]:
        return {self.result_name(): self.result_var}

    @property
    def result_type(self) -> QuantumType:
        assert self._result_type is not None
        return self._result_type

    @classmethod
    @abc.abstractmethod
    def result_name(cls) -> str:
        raise NotImplementedError()
