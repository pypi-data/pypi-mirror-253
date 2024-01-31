from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.functions.classical_type import Bool, Integer
from classiq.interface.generator.functions.port_declaration import (
    PortDeclarationDirection,
)
from classiq.interface.helpers.pydantic_model_helpers import nameables_to_dict
from classiq.interface.model.port_declaration import PortDeclaration
from classiq.interface.model.quantum_function_declaration import (
    QuantumFunctionDeclaration,
    QuantumOperandDeclaration,
)
from classiq.interface.model.quantum_type import QuantumInteger

REPEAT_OPERATOR = QuantumFunctionDeclaration(
    name="repeat",
    param_decls={"count": Integer()},
    operand_declarations={
        "iteration": QuantumOperandDeclaration(
            name="iteration", param_decls={"index": Integer()}
        )
    },
)

OPERAND_FIELD_NAME = "operand"


INVERT_OPERATOR = QuantumFunctionDeclaration(
    name="invert",
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(name=OPERAND_FIELD_NAME)
    },
)


CONTROL_OPERATOR = QuantumFunctionDeclaration(
    name="control",
    port_declarations={
        "ctrl": PortDeclaration(
            name="ctrl",
            direction=PortDeclarationDirection.Inout,
        )
    },
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(name=OPERAND_FIELD_NAME)
    },
)

IF_OPERATOR = QuantumFunctionDeclaration(
    name="if",
    param_decls={"condition": Bool()},
    operand_declarations={
        "then": QuantumOperandDeclaration(name="then"),
        "else": QuantumOperandDeclaration(name="else"),
    },
)

SWITCH_OPERATOR = QuantumFunctionDeclaration(
    name="switch",
    param_decls={"selector": Integer()},
    operand_declarations={
        "cases": QuantumOperandDeclaration(
            name="cases",
            is_list=True,
        )
    },
)


JOIN_OPERATOR = QuantumFunctionDeclaration(
    name="join",
    port_declarations={
        "in1": PortDeclaration(name="in1", direction="input"),
        "in2": PortDeclaration(name="in2", direction="input"),
        "out": PortDeclaration(
            name="out",
            direction="output",
            size=Expression(expr="len(in1)+len(in2)"),
        ),
    },
)


SPLIT_OPERATOR = QuantumFunctionDeclaration(
    name="split",
    param_decls={"out1_size": Integer(), "out2_size": Integer()},
    port_declarations={
        "in": PortDeclaration(
            name="in",
            direction="input",
            size=Expression(expr="out1_size+out2_size"),
        ),
        "out1": PortDeclaration(
            name="out1", direction="output", size=Expression(expr="out1_size")
        ),
        "out2": PortDeclaration(
            name="out2", direction="output", size=Expression(expr="out2_size")
        ),
    },
)


PERMUTE_OPERATOR = QuantumFunctionDeclaration(
    name="permute",
    operand_declarations={
        "functions": QuantumOperandDeclaration(
            name="functions",
            is_list=True,
        )
    },
)


POWER_OPERATOR = QuantumFunctionDeclaration(
    name="power",
    param_decls={"power": Integer()},
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(name=OPERAND_FIELD_NAME)
    },
)


CONTROL_WITH_VALUE_OPERATOR = QuantumFunctionDeclaration(
    name="control_with_value",
    param_decls={"ctrl_val": Integer()},
    port_declarations={
        "ctrl": PortDeclaration(
            name="ctrl",
            quantum_type=QuantumInteger(),
            direction=PortDeclarationDirection.Inout,
        )
    },
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(name=OPERAND_FIELD_NAME)
    },
)

APPLY = QuantumFunctionDeclaration(
    name="apply",
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(
            name=OPERAND_FIELD_NAME,
        )
    },
)


COMPUTE = QuantumFunctionDeclaration(
    name="compute",
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(
            name=OPERAND_FIELD_NAME,
        )
    },
)


UNCOMPUTE = QuantumFunctionDeclaration(
    name="uncompute",
    operand_declarations={
        OPERAND_FIELD_NAME: QuantumOperandDeclaration(
            name=OPERAND_FIELD_NAME,
        )
    },
)


BUILTIN_QUANTUM_OPERATOR_LIST = [
    REPEAT_OPERATOR,
    INVERT_OPERATOR,
    CONTROL_OPERATOR,
    IF_OPERATOR,
    SWITCH_OPERATOR,
    JOIN_OPERATOR,
    SPLIT_OPERATOR,
    PERMUTE_OPERATOR,
    POWER_OPERATOR,
    CONTROL_WITH_VALUE_OPERATOR,
    APPLY,
    COMPUTE,
    UNCOMPUTE,
]


QuantumFunctionDeclaration.BUILTIN_FUNCTION_DECLARATIONS.update(
    nameables_to_dict(BUILTIN_QUANTUM_OPERATOR_LIST)
)
