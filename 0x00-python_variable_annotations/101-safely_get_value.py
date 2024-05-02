#!/usr/bin/env python3
"""
Annotated function
"""

from typing import TypeVar, Mapping, Any, Union

# Define a type variable ~T to represent the type of the default value
T = TypeVar('~T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return the value associated with the key in the dictionary if exists"""
    if key in dct:
        return dct[key]
    else:
        return default
