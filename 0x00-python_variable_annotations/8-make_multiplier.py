#!/usr/bin/env python3

"""This module contains a function that manipulate complex types
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function creates a new function
    param: float
    return: A function
    """
    def multiplier_func(x: float) -> float:
        return multiplier * x
    return multiplier_func
