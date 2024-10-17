#!/usr/bin/env python3

"""This module contains a fonction that works with ducked types
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function make a simple verification on a sequence
    param: lst
    return: None of a Any
    """
    if lst:
        return lst[0]
    else:
        return None
