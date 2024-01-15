#!/usr/bin/env python3
"""Import wait_n from 2-measure_runtime."""
import asyncio
import time
wait_n = __import__('2-measure_runtime').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of wait_n."""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
