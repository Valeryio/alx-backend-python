#!/usr/bin/env python3

"""This module contains a functin othat get values from a
dict
"""


from typing import Union, Any, TypeVar, Mapping, Generic

T = TypeVar('T', covariant=True)
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
