#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(n: int, max_delay: int) -> List[asyncio.Task]:
    """ Spawn wait_random n times with max_delay."""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]

task_wait_random()
