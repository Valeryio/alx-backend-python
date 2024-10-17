#!/usr/bin/env python3

"""This module contains a type-annotated function floor that
returns floor of entry arguments
"""

from math import floor as used_floor


def floor(n: float) -> int:
    """
    this function return the floor of a float
    param: n
    return: an integer
    """
    return used_floor(n)
