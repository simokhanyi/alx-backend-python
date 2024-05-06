#!/usr/bin/env python3
""" code that alter wait_n into a new function """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for multiple random delays asynchronously.

    Args:
        n (int): Number of delays to wait for.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of random delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)


# Test the function
if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
