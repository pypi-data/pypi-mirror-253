from typing import Tuple, Union

from classiq.interface.generator.arith import number_utils
from classiq.interface.generator.arith.register_user_input import RegisterArithmeticInfo

RegisterOrConst = Union[RegisterArithmeticInfo, float]


def fraction_places(argument: RegisterOrConst, *, machine_precision: int) -> int:
    if isinstance(argument, RegisterArithmeticInfo):
        return argument.fraction_places
    return number_utils.fraction_places(argument, machine_precision=machine_precision)


def integer_part_size(argument: RegisterOrConst) -> int:
    if isinstance(argument, RegisterArithmeticInfo):
        return argument.integer_part_size
    return number_utils.integer_part_size(argument)


def size(argument: RegisterOrConst, *, machine_precision: int) -> int:
    if isinstance(argument, RegisterArithmeticInfo):
        return argument.size
    return number_utils.size(argument, machine_precision=machine_precision)


def is_signed(argument: RegisterOrConst) -> bool:
    if isinstance(argument, RegisterArithmeticInfo):
        return argument.is_signed
    return argument < 0


def upper_bound(argument: RegisterOrConst) -> float:
    if isinstance(argument, RegisterArithmeticInfo):
        return max(argument.bounds)
    return argument


def lower_bound(argument: RegisterOrConst) -> float:
    if isinstance(argument, RegisterArithmeticInfo):
        return min(argument.bounds)
    return argument


def bounds(argument: RegisterOrConst) -> Tuple[float, float]:
    if isinstance(argument, RegisterArithmeticInfo):
        return argument.bounds
    return argument, argument
