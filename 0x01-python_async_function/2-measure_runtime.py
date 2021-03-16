#!/usr/bin/env python3
""" measure_time module """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ measure_time module """
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    e = time.time()
    return ((e - s) / n)
