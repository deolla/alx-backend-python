#!/usr/bin/env python3
"""A type-annotated function make_multipler."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiplier_func(m: float) -> float:
        """Multiplies a float by multiplier"""
        return m * multiplier

    return multiplier_func
