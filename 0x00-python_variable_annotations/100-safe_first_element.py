#!/usr/bin/env python3
""" make_multiplier module """
import typing


def safe_first_element(lst:
                       typing.Sequence[typing.Any]) -> typing.Union[
        typing.Any, NoneType]:
    """ safe_first_element module """
    if lst:
        return lst[0]
    else:
        return None
