#!/usr/bin/env python3
""" to_kv module """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ to_kv module """
    return ((k, v*v,))
