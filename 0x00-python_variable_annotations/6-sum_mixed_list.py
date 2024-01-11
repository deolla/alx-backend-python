#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float."""
    return sum(mxd_lst)
