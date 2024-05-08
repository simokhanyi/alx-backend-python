#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using an async comprehensing
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over
    async_generator.

    Returns:
        List[float]: A list containing 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]
