#!/usr/bin/env python3
"""Import wait_n to 2-measure_runtime."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)."""
    start_time = time.time()
    delay = wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
