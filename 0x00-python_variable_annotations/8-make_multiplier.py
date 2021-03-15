#!/usr/bin/env python3
""" make_multiplier module """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ make_multiplier module """
    def mult(x: float) -> float:
        """ make_multiplier module """
        return (multiplier * x)
    return (mult)
