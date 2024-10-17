#!/usr/bin/env python3

"""THis module contain a function typed with complex structure
like list
"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """It sum the different element of a list
    param: input_list
    return: a float
    """
    result: float = reduce(lambda x, y: x + y, input_list)
    return result
