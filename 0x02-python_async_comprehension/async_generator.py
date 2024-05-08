#!/usr/bin/env python3
"""
Coroutine that loop 10 times, each time asynchronously wait 1 second
then yield a random number between 0 and 10
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that asynchronously generates random numbers.

    This coroutine loops 10 times, each time asynchronously waiting
    for 1 second and then yielding a random number between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
