#!/usr/bin/env python3
"""
Modules Imported: typing

typing: access several default/non-default data types

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a Callable

    Args:
    multiplier(float): a float obj

    Return:
    A callable function that multiplies multiplier by another arg

    """
    def multiply_multiplier(multiplier: float) -> float:
        return multiplier * multiplier
    return multiply_multiplier
