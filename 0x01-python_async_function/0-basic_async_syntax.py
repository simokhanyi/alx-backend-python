#!/usr/bin/env python3
""" 
An asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds.

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


# Test the coroutine
if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
