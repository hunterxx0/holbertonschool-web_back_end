#!/usr/bin/env python3
""" make_multiplier module """
import typing


def safely_get_value(dct: typing.Mapping,
                     key: typing.Any,
                     default: typing.Union[typing.TypeVar('T'),
                                           None] = None) -> typing.Union[
        typing.Any,
        typing.TypeVar('T')]:
    """ safe_first_element module """
    if key in dct:
        return dct[key]
    else:
        return default
