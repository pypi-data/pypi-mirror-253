# This file was generated automatically - do not edit manually

from typing import List, Literal

from classiq.qmod.qmod_parameter import QParam
from classiq.qmod.qmod_variable import Input, Output, QArray, QBit, QNum
from classiq.qmod.quantum_callable import QCallable
from classiq.qmod.quantum_function import ExternalQFunc

from .structs import *


@ExternalQFunc
def H(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def X(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def Y(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def Z(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def I(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def S(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def T(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def SDG(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def TDG(
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def PHASE(
    theta: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def RX(
    theta: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def RY(
    theta: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def RZ(
    theta: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def R(
    theta: QParam[float],
    phi: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def RXX(
    theta: QParam[float],
    target: QArray[QBit, Literal[2]],
) -> None:
    pass


@ExternalQFunc
def RYY(
    theta: QParam[float],
    target: QArray[QBit, Literal[2]],
) -> None:
    pass


@ExternalQFunc
def RZZ(
    theta: QParam[float],
    target: QArray[QBit, Literal[2]],
) -> None:
    pass


@ExternalQFunc
def CH(
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CX(
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CY(
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CZ(
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CRX(
    theta: QParam[float],
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CRY(
    theta: QParam[float],
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CRZ(
    theta: QParam[float],
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CPHASE(
    theta: QParam[float],
    control: QBit,
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def SWAP(
    qbit0: QBit,
    qbit1: QBit,
) -> None:
    pass


@ExternalQFunc
def IDENTITY(
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def prepare_state(
    probabilities: QParam[List[float]],
    bound: QParam[float],
    out: Output[QArray[QBit, Literal["log(len(probabilities), 2)"]]],
) -> None:
    pass


@ExternalQFunc
def prepare_amplitudes(
    amplitudes: QParam[List[float]],
    bound: QParam[float],
    out: Output[QArray[QBit, Literal["log(len(amplitudes), 2)"]]],
) -> None:
    pass


@ExternalQFunc
def unitary(
    elements: QParam[List[List[float]]],
    target: QArray[QBit, Literal["log(len(elements[0]), 2)"]],
) -> None:
    pass


@ExternalQFunc
def add(
    left: QArray[QBit],
    right: QArray[QBit],
    result: Output[QArray[QBit, Literal["Max(len(left), len(right)) + 1"]]],
) -> None:
    pass


@ExternalQFunc
def U(
    theta: QParam[float],
    phi: QParam[float],
    lam: QParam[float],
    gam: QParam[float],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def CCX(
    control: QArray[QBit, Literal[2]],
    target: QBit,
) -> None:
    pass


@ExternalQFunc
def allocate(
    num_qubits: QParam[int],
    out: Output[QArray[QBit, Literal["num_qubits"]]],
) -> None:
    pass


@ExternalQFunc
def free(
    in_: Input[QArray[QBit]],
) -> None:
    pass


@ExternalQFunc
def randomized_benchmarking(
    num_of_cliffords: QParam[int],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def inplace_prepare_state(
    probabilities: QParam[List[float]],
    bound: QParam[float],
    target: QArray[QBit, Literal["log(len(probabilities), 2)"]],
) -> None:
    pass


@ExternalQFunc
def inplace_prepare_amplitudes(
    amplitudes: QParam[List[float]],
    bound: QParam[float],
    target: QArray[QBit, Literal["log(len(amplitudes), 2)"]],
) -> None:
    pass


@ExternalQFunc
def single_pauli_exponent(
    pauli_string: QParam[List[int]],
    coefficient: QParam[float],
    qbv: QArray[QBit, Literal["len(pauli_string)"]],
) -> None:
    pass


@ExternalQFunc
def suzuki_trotter(
    pauli_operator: QParam[List[PauliTerm]],
    evolution_coefficient: QParam[float],
    order: QParam[int],
    repetitions: QParam[int],
    qbv: QArray[QBit, Literal["len(get_field(pauli_operator[0], 'pauli'))"]],
) -> None:
    pass


@ExternalQFunc
def qdrift(
    pauli_operator: QParam[List[PauliTerm]],
    evolution_coefficient: QParam[float],
    num_qdrift: QParam[int],
    qbv: QArray[QBit, Literal["len(get_field(pauli_operator[0], 'pauli'))"]],
) -> None:
    pass


@ExternalQFunc
def exponentiation_with_depth_constraint(
    pauli_operator: QParam[List[PauliTerm]],
    evolution_coefficient: QParam[float],
    max_depth: QParam[int],
    qbv: QArray[QBit, Literal["len(get_field(pauli_operator[0], 'pauli'))"]],
) -> None:
    pass


@ExternalQFunc
def qft_step(
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def qft(
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def standard_qpe(
    precision: QParam[int],
    unitary: QCallable,
    phase: QArray[QBit, Literal["precision"]],
) -> None:
    pass


@ExternalQFunc
def qpe(
    precision: QParam[int],
    unitary: QCallable,
    phase: Output[QArray[QBit, Literal["precision"]]],
) -> None:
    pass


@ExternalQFunc
def single_pauli(
    slope: QParam[float],
    offset: QParam[float],
    q1_qfunc: QCallable[QParam[float], QBit],
    x: QArray[QBit],
    q: QBit,
) -> None:
    pass


@ExternalQFunc
def linear_pauli_rotations(
    bases: QParam[List[int]],
    slopes: QParam[List[float]],
    offsets: QParam[List[float]],
    x: QArray[QBit],
    q: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def amplitude_estimation(
    num_phase_qubits: QParam[int],
    num_unitary_qubits: QParam[int],
    sp_op: QCallable[QParam[int], QArray[QBit, Literal["num_unitary_qubits"]]],
    oracle_op: QCallable[QParam[int], QArray[QBit, Literal["num_unitary_qubits"]]],
    phase_port: Output[QArray[QBit, Literal["num_phase_qubits"]]],
    unitary_port: Output[QArray[QBit, Literal["num_unitary_qubits"]]],
) -> None:
    pass


@ExternalQFunc
def simple_oracle(
    predicate: QCallable[QArray[QBit, Literal["len(target)"]], QBit],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def grover_diffuser(
    num_qubits: QParam[int],
    p: QArray[QBit, Literal["num_qubits"]],
) -> None:
    pass


@ExternalQFunc
def grover_operator(
    num_qubits: QParam[int],
    sp_op: QCallable[QParam[int], QArray[QBit, Literal["num_qubits"]]],
    oracle_op: QCallable[QParam[int], QArray[QBit, Literal["num_qubits"]]],
    p: QArray[QBit, Literal["num_qubits"]],
) -> None:
    pass


@ExternalQFunc
def hadamard_transform(
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def apply_to_all(
    gate_operand: QCallable[QBit],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def grover_search(
    num_qubits: QParam[int],
    reps: QParam[int],
    oracle_op: QCallable[QParam[int], QArray[QBit, Literal["num_qubits"]]],
    gsq: QArray[QBit, Literal["num_qubits"]],
) -> None:
    pass


@ExternalQFunc
def prepare_int(
    val: QParam[int],
    out: Output[QNum],
) -> None:
    pass


@ExternalQFunc
def allocate_num(
    num_qubits: QParam[int],
    is_signed: QParam[bool],
    fraction_digits: QParam[int],
    out: Output[QNum],
) -> None:
    pass


@ExternalQFunc
def qaoa_mixer_layer(
    b: QParam[float],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def qaoa_cost_layer(
    g: QParam[float],
    hamiltonian: QParam[List[PauliTerm]],
    is_st: QParam[bool],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def qaoa_layer(
    g: QParam[float],
    b: QParam[float],
    hamiltonian: QParam[List[PauliTerm]],
    is_st: QParam[bool],
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def qaoa_init(
    target: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def qaoa_penalty(
    num_qubits: QParam[int],
    params_list: QParam[List[float]],
    hamiltonian: QParam[List[PauliTerm]],
    is_st: QParam[bool],
    target: QArray[QBit, Literal["num_qubits"]],
) -> None:
    pass


@ExternalQFunc
def full_hea(
    num_qubits: QParam[int],
    is_parametrized: QParam[List[int]],
    angle_params: QParam[List[float]],
    connectivity_map: QParam[List[List[int]]],
    reps: QParam[int],
    operands_1qubit: QCallable[QParam[float], QBit],
    operands_2qubit: QCallable[QParam[float], QBit, QBit],
    x: QArray[QBit, Literal["num_qubits"]],
) -> None:
    pass


@ExternalQFunc
def repeat(
    count: QParam[int],
    iteration: QCallable[QParam[int]],
) -> None:
    pass


@ExternalQFunc
def invert(
    operand: QCallable,
) -> None:
    pass


@ExternalQFunc
def control(
    operand: QCallable,
    ctrl: QArray[QBit],
) -> None:
    pass


@ExternalQFunc
def if_(
    condition: QParam[bool],
    then: QCallable,
    else_: QCallable,
) -> None:
    pass


@ExternalQFunc
def switch(
    selector: QParam[int],
    cases: QCallable,
) -> None:
    pass


@ExternalQFunc
def join(
    in1: Input[QArray[QBit]],
    in2: Input[QArray[QBit]],
    out: Output[QArray[QBit, Literal["len(in1)+len(in2)"]]],
) -> None:
    pass


@ExternalQFunc
def split(
    out1_size: QParam[int],
    out2_size: QParam[int],
    in_: Input[QArray[QBit, Literal["out1_size+out2_size"]]],
    out1: Output[QArray[QBit, Literal["out1_size"]]],
    out2: Output[QArray[QBit, Literal["out2_size"]]],
) -> None:
    pass


@ExternalQFunc
def permute(
    functions: QCallable,
) -> None:
    pass


@ExternalQFunc
def power(
    power: QParam[int],
    operand: QCallable,
) -> None:
    pass


@ExternalQFunc
def control_with_value(
    ctrl_val: QParam[int],
    operand: QCallable,
    ctrl: QNum,
) -> None:
    pass


@ExternalQFunc
def apply(
    operand: QCallable,
) -> None:
    pass


@ExternalQFunc
def compute(
    operand: QCallable,
) -> None:
    pass


@ExternalQFunc
def uncompute(
    operand: QCallable,
) -> None:
    pass


@ExternalQFunc
def molecule_ucc(
    molecule_problem: QParam[MoleculeProblem],
    excitations: QParam[List[int]],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(molecule_problem_to_hamiltonian(molecule_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def molecule_hva(
    molecule_problem: QParam[MoleculeProblem],
    reps: QParam[int],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(molecule_problem_to_hamiltonian(molecule_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def molecule_hartree_fock(
    molecule_problem: QParam[MoleculeProblem],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(molecule_problem_to_hamiltonian(molecule_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def fock_hamiltonian_ucc(
    fock_hamiltonian_problem: QParam[FockHamiltonianProblem],
    excitations: QParam[List[int]],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(fock_hamiltonian_problem_to_hamiltonian(fock_hamiltonian_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def fock_hamiltonian_hva(
    fock_hamiltonian_problem: QParam[FockHamiltonianProblem],
    reps: QParam[int],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(fock_hamiltonian_problem_to_hamiltonian(fock_hamiltonian_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def fock_hamiltonian_hartree_fock(
    fock_hamiltonian_problem: QParam[FockHamiltonianProblem],
    qbv: QArray[
        QBit,
        Literal[
            "len(get_field(fock_hamiltonian_problem_to_hamiltonian(fock_hamiltonian_problem)[0], 'pauli'))"
        ],
    ],
) -> None:
    pass


@ExternalQFunc
def log_normal_finance(
    finance_model: QParam[LogNormalModel],
    finance_function: QParam[FinanceFunction],
    func_port: QArray[QBit, Literal["get_field(finance_model, 'num_qubits')"]],
    obj_port: QBit,
) -> None:
    pass


@ExternalQFunc
def gaussian_finance(
    finance_model: QParam[GaussianModel],
    finance_function: QParam[FinanceFunction],
    func_port: QArray[
        QBit,
        Literal[
            "get_field(finance_model, 'num_qubits') + len(get_field(finance_model, 'rhos')) + floor(log(sum(get_field(finance_model, 'loss')), 2)) + 1"
        ],
    ],
    obj_port: QBit,
) -> None:
    pass


@ExternalQFunc
def pauli_feature_map(
    feature_map: QParam[QSVMFeatureMapPauli],
    qbv: QArray[QBit, Literal["get_field(feature_map, 'feature_dimension')"]],
) -> None:
    pass


@ExternalQFunc
def bloch_sphere_feature_map(
    feature_dimension: QParam[int],
    qbv: QArray[QBit, Literal["ceiling(feature_dimension/2)"]],
) -> None:
    pass


__all__ = [
    "H",
    "X",
    "Y",
    "Z",
    "I",
    "S",
    "T",
    "SDG",
    "TDG",
    "PHASE",
    "RX",
    "RY",
    "RZ",
    "R",
    "RXX",
    "RYY",
    "RZZ",
    "CH",
    "CX",
    "CY",
    "CZ",
    "CRX",
    "CRY",
    "CRZ",
    "CPHASE",
    "SWAP",
    "IDENTITY",
    "prepare_state",
    "prepare_amplitudes",
    "unitary",
    "add",
    "U",
    "CCX",
    "allocate",
    "free",
    "randomized_benchmarking",
    "inplace_prepare_state",
    "inplace_prepare_amplitudes",
    "single_pauli_exponent",
    "suzuki_trotter",
    "qdrift",
    "exponentiation_with_depth_constraint",
    "qft_step",
    "qft",
    "standard_qpe",
    "qpe",
    "single_pauli",
    "linear_pauli_rotations",
    "amplitude_estimation",
    "simple_oracle",
    "grover_diffuser",
    "grover_operator",
    "hadamard_transform",
    "apply_to_all",
    "grover_search",
    "prepare_int",
    "allocate_num",
    "qaoa_mixer_layer",
    "qaoa_cost_layer",
    "qaoa_layer",
    "qaoa_init",
    "qaoa_penalty",
    "full_hea",
    "repeat",
    "invert",
    "control",
    "if_",
    "switch",
    "join",
    "split",
    "permute",
    "power",
    "control_with_value",
    "apply",
    "compute",
    "uncompute",
    "molecule_ucc",
    "molecule_hva",
    "molecule_hartree_fock",
    "fock_hamiltonian_ucc",
    "fock_hamiltonian_hva",
    "fock_hamiltonian_hartree_fock",
    "log_normal_finance",
    "gaussian_finance",
    "pauli_feature_map",
    "bloch_sphere_feature_map",
]
