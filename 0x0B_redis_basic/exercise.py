#!/usr/bin/env python3
"""
Cache module
"""
from functools import wraps
import redis
from typing import Union, Any, Optional, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    Counts calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper fun
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Creates input and output list keys
    """
    @wraps(method)
    def wrapper(self, *args):
        """wrapper func"""
        self._redis.rpush(
            "{}:inputs".format(method.__qualname__),
            str(args))
        res = method(self, *args)
        self._redis.rpush(
            "{}:outputs".format(method.__qualname__),
            str(res))
        return res
    return wrapper


def replay(method: Callable) -> str:
    """
    display the history of calls of a function
    """
    func = method.__qualname__
    inps = method.__self__._redis.lrange(
        "{}:inputs".format(func), 0, -1)
    outs = method.__self__._redis.lrange(
        "{}:outputs".format(func), 0, -1)
    ct = method.__self__._redis.get(func)
    print("{} was called {} times:".format(func, ct.decode('utf-8')))
    for i, o in zip(inps, outs):
        print("{}(*{}) -> {}".format(
            func, i.decode('utf-8'), o.decode('utf-8')))


class Cache:
    """
    Stores an instance of the Redis client as a private variable
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: str) -> Union[str, int, float, bytes]:
        """
        Generate a random key, stores the input data in Redis
        using the key.
        """
        red = self._redis
        key = str(uuid4())
        red[key] = data
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Returns the Key value with the right data type
        """
        res = self._redis.get(key)
        if res:
            if fn:
                res = fn(res)
        return res

    def get_str(self, key: str) -> Any:
        """
        automatically parametrize Cache.get
        with the correct conversion function.
        """
        return self.get(key, int)

    def get_int(self, key: int) -> Any:
        """
        automatically parametrize Cache.get
        with the correct conversion function.
        """
        return self.get(key, int)
