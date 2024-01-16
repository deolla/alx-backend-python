#!/usr/bin/env python3
"""Import async_comprehension frm previous file."""
import asyncio
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it."""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    return total_time
