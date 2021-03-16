#!/usr/bin/env python3
""" wait_random module """
import asyncio
import random


async def wait_random(max_delay=10.0):
    """ wait_random module """
    a = random.uniform(0.0, max_delay)
    await asyncio.sleep(a)
    return a