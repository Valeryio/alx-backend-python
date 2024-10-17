#!/usr/bin/env python3

"""THis module contains a function that takes a string
and returns a tuple
"""

from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """It use a string and a number to create a tuple
    param: k
    param: v
    return: A tuple
    """
    result: Tuple = (k, v*v)
    return result
