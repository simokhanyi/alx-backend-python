#!/usr/bin/env python3
"""
A function that takes an integer max_delay and returns a asyncio
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a asyncio.Task for waiting for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task representing the asynchronous operation.
    """
    coro = wait_random(max_delay)
    return asyncio.create_task(coro)


# Test the function
if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
