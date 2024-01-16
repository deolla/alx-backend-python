#!/usr/bin/env python3
"""Write a coroutine called async_generator"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, asynchronously wait 1 sec, yield a rand num."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
