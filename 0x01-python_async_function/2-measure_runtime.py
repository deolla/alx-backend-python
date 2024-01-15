#!/usr/bin/env python3
"""Import wait_n to 2-measure_runtime."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds.
    :return: Average time per iteration in seconds.
    """
    start_time = time.time()

    # Asynchronously execute wait_n
    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    # Return the average time per iteration
    return total_time / n
