#!/usr/bin/env python3
""" make_multiplier module """
import typing


def mult(x):
    """ make_multiplier module """
    return (x * x)


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ make_multiplier module """
    return (mult)
