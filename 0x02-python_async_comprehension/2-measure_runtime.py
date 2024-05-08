#!/usr/bin/env python3
""" async comprehesion """

import asyncio
from typing import Coroutine
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
