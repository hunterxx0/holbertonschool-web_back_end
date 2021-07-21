#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine
that will execute async_comprehension four times in parallel
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime and return it.
    """
    s = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - s
