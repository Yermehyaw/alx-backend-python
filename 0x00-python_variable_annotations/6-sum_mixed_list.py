#!/usr/bin/env python3
"""
Modules Imported: None

"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    Returns sum of list of mixed data types

    Args:
    mxd_lst(list): list of int and floats

    """
    sum: float = 0.0
    for value in mxd_lst:
        sum += float(value)
    return sum
