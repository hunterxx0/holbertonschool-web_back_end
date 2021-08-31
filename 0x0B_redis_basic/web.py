#!/usr/bin/env python3
"""
Web module
"""

import redis
import requests


redis = redis.Redis()


def get_page(url: str) -> str:
    """
    Counts calls
    """
    key = "count:{}".format(url)
    redis.setex(key, 10, 0)
    r = requests.get(url)
    redis.incr(key)
    return r.text


res = get_page("http://slowwly.robertomurray.co.uk")
print(res)
