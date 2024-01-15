#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(n: int, max_delay: int) -> List[asyncio.Task]:
    """ Returns a list of tasks."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return tasks
