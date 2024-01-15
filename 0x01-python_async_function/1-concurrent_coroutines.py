#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with max_delay."""
    delays = []
    tasks = [wait_random(n, max_delay) for n in range(n)]
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
