#!/usr/bin/env python3
""" wait_random module """
import asyncio
import random
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ wait_random module """
    ll: typing.List[float] = [await wait_random(max_delay) for i in range(n)]
    return ll
