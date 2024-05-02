#!/usr/bin/env python3
"""
Annotated function
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Return first element of the sequence if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
