#!/usr/bin/env python3

"""
THis module contains a function that sums a complex list
"""

from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """It computes the calculation of different number types
    param: mxd_lst
    return: a float
    """
    result: float = reduce(lambda x, y: x + y, mxd_lst)
    return result
