#!/usr/bin/env python3
"""
function sum_list which takes a list input_list of floats
as argument and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of integers and floats in the mixed list."""
    return sum(mxd_lst)
