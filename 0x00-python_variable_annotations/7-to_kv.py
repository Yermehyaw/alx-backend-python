#!/usr/bin/env python3
"""
Modules Imported: None

typing: Provide types for py and earlier
"""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    Return a new tuple

    Args: 
    k(str): string
    v(int | float): int or float data obj

    """
    return k, v * v
