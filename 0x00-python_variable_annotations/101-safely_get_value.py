#!/usr/bin/env python3
"""Add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dit: Mapping,
                     key: Any, default: Union[T, None]
                    ) -> Union[Any, T]:
    """Add type annotations to the function"""
    if key in dit:
        return dit[key]
    else:
        return default
