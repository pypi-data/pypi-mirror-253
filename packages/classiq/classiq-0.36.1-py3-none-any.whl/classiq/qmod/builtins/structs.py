# This file was generated automatically - do not edit manually

from typing import List

from classiq.qmod.qmod_struct import QStruct


@QStruct
class PauliTerm:
    pauli: List[int]
    coefficient: float


@QStruct
class MoleculeProblem:
    mapping: int
    z2_symmetries: bool
    molecule: "Molecule"
    freeze_core: bool
    remove_orbitals: List[int]


@QStruct
class Molecule:
    atoms: List["ChemistryAtom"]
    spin: int
    charge: int


@QStruct
class ChemistryAtom:
    element: int
    position: "Position"


@QStruct
class Position:
    x: float
    y: float
    z: float


@QStruct
class FockHamiltonianProblem:
    mapping: int
    z2_symmetries: bool
    terms: List["LadderTerm"]
    num_particles: List[int]


@QStruct
class LadderTerm:
    coefficient: float
    ops: List["LadderOp"]


@QStruct
class LadderOp:
    op: int
    index: int


@QStruct
class CombinatorialOptimizationSolution:
    probability: float
    cost: float
    solution: List[int]
    count: int


@QStruct
class GaussianModel:
    num_qubits: int
    normal_max_value: float
    default_probabilities: List[float]
    rhos: List[float]
    loss: List[int]
    min_loss: int


@QStruct
class LogNormalModel:
    num_qubits: int
    mu: float
    sigma: float


@QStruct
class FinanceFunction:
    f: int
    threshold: float
    larger: bool
    polynomial_degree: int
    use_chebyshev_polynomial_approximation: bool
    tail_probability: float


@QStruct
class QsvmResult:
    test_score: float
    predicted_labels: List[float]


@QStruct
class QSVMFeatureMapPauli:
    feature_dimension: int
    reps: int
    entanglement: int
    alpha: float
    paulis: List[List[int]]


__all__ = [
    "PauliTerm",
    "MoleculeProblem",
    "Molecule",
    "ChemistryAtom",
    "Position",
    "FockHamiltonianProblem",
    "LadderTerm",
    "LadderOp",
    "CombinatorialOptimizationSolution",
    "GaussianModel",
    "LogNormalModel",
    "FinanceFunction",
    "QsvmResult",
    "QSVMFeatureMapPauli",
]
