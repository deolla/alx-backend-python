#!/usr/bin/env python3
"""A type-annotated function sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return their sum as a float."""
    return sum(input_list)
