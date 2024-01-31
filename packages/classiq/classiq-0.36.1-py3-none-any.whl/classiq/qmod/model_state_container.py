from typing import Dict

from classiq.interface.model.native_function_definition import NativeFunctionDefinition

from classiq import StructDeclaration


class ModelStateContainer:
    type_decls: Dict[str, StructDeclaration]
    native_defs: Dict[str, NativeFunctionDefinition]


QMODULE = ModelStateContainer()
