#!/usr/bin/env python3
""" task_wait_n module """
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ task_wait_n module """
    ll: typing.List[float] = [await task_wait_random(max_delay)
                              for i in range(n)]
    return sorted(ll)
