#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for multiple random delays asynchronously.

    Args:
        n (int): Number of delays to wait for.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of random delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)

# Test the coroutine
if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
