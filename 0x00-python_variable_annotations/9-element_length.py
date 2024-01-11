#!/usr/bin/env python3
"""Annotate the below function’s parameters, return values"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of the elements of a list"""
    return [(i, len(i)) for i in lst]
