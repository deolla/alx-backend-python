#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    :param max_delay: Maximum delay in seconds (default is 10).
    :return: Random delay between 0 and max_delay.
    """
    # Generate a random delay within the specified range
    delay = random.uniform(0, max_delay)

    # Use asyncio.sleep to asynchronously wait for the generated delay
    await asyncio.sleep(delay)

    return delay
