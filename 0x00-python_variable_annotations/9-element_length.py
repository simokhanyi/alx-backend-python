#!/usr/bin/env python3
"""
Annotated function
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element of lst, its length."""
    return [(i, len(i)) for i in lst]
