from typing import Any, List, Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated, TypeAlias

from classiq.interface.executor.iqae_result import IQAEResult
from classiq.interface.executor.result import EstimationResult, ExecutionDetails
from classiq.interface.executor.vqe_result import VQESolverResult
from classiq.interface.helpers.versioned_model import VersionedModel

from classiq._internals.enum_utils import StrEnum


class SavedResultValueType(StrEnum):
    Integer = "int"
    Float = "float"
    Boolean = "bool"
    VQESolverResult = "VQESolverResult"
    ExecutionDetails = "ExecutionDetails"
    EstimationResult = "EstimationResult"
    IQAEResult = "IQAEResult"
    Unstructured = "Unstructured"


class TaggedInteger(BaseModel):
    value_type: Literal[SavedResultValueType.Integer]
    name: str
    value: int


class TaggedFloat(BaseModel):
    value_type: Literal[SavedResultValueType.Float]
    name: str
    value: float


class TaggedBoolean(BaseModel):
    value_type: Literal[SavedResultValueType.Boolean]
    name: str
    value: bool


class TaggedVQESolverResult(BaseModel):
    value_type: Literal[SavedResultValueType.VQESolverResult]
    name: str
    value: VQESolverResult


class TaggedExecutionDetails(BaseModel):
    value_type: Literal[SavedResultValueType.ExecutionDetails]
    name: str
    value: ExecutionDetails


class TaggedEstimationResult(BaseModel):
    value_type: Literal[SavedResultValueType.EstimationResult]
    name: str
    value: EstimationResult


class TaggedIQAEResult(BaseModel):
    value_type: Literal[SavedResultValueType.IQAEResult]
    name: str
    value: IQAEResult


class TaggedUnstructured(BaseModel):
    value_type: Literal[SavedResultValueType.Unstructured]
    name: str
    value: Any


SavedResult = Annotated[
    Union[
        TaggedInteger,
        TaggedFloat,
        TaggedBoolean,
        TaggedVQESolverResult,
        TaggedExecutionDetails,
        TaggedEstimationResult,
        TaggedIQAEResult,
        TaggedUnstructured,
    ],
    Field(..., discriminator="value_type"),
]

ResultsCollection: TypeAlias = List[SavedResult]


class ExecuteGeneratedCircuitResults(VersionedModel):
    results: ResultsCollection
