#!/usr/bin/env python3

"""This module contains a function that return the length of
an iterable
"""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """It manipulate an iterable
    param: lst
    return: a tuple
    """
    return [(i, len(i)) for i in lst]
