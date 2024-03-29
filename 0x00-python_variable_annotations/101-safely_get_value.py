#!/usr/bin/env python3
"""Add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any, default: Union[T, None]
) -> Union[Any, T]:
    """Add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
