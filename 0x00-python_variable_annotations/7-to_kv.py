#!/usr/bin/env python3
"""
annotated function to_kv that takes a string k and an int OR float
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and the second v."""
    return (k, v ** 2)
