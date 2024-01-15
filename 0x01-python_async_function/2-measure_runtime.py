#!/usr/bin/env python3
""" Import wait_n into 2-measure_runtime.py."""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay):
    """Measure the runtime."""
    begin = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return (end - begin) / n
