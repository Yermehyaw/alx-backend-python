#!/usr/bin/env python3
"""
Modules Imported: None

"""


sum: float = 0.0
def sum_list(input_list: list[float]) -> float:
    for elem in input_list:
        sum += elem
    return sum
