#!/usr/bin/env python3
"""
Modules Imported: typing

typing: access default and non-default type hints

"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of list of mixed data types

    Args:
    mxd_lst(list): list of int and floats

    """
    return sum(mxd_lst)
