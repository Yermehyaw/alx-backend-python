#!/usr/bin/env python3
"""
Duck type the parameters and return values of a function

Modules Imported: typing

typing: Provides custom data types

"""
from typing import Iterator
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Utilize abstract types for annotating a func

    Args:
    lst(Iterable): Any iterable object

    Return:
    An abstract list of abstract tuple of a sequence
    """
    # temp = []
    return [(i, len(i)) for i in lst]
