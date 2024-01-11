#!/usr/bin/env python3
"""A type-annotated function to_kv, takes string k and int/float v"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return k, v * v   # return k, v ** 2.0
