#!/usr/bin/env python3
"""
Modules Imported: typing

typing: access default ans non-default hint types

"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns sum of floats

    Args:
    input_list(list): list of floats

    """
    return sum(input_list)
