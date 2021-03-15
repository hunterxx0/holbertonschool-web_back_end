#!/usr/bin/env python3
""" make_multiplier module """
import typing

def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """ element_length module """
    return [(i, len(i)) for i in lst]
