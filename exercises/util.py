from typing import Union


def add_two_numbers(num_one, num_two):
    print(__name__)
    return num_one + num_two


def subtract_two_numbers(
    num_one: Union[float, int], num_two: Union[float, int]
) -> Union[float, int]:
    print(__name__)
    return num_one - num_two
