#!/usr/bin/env python3
"""
Modules Imported: None

typing: Provide types for py and earlier
"""
from typing import Union


def to_kv(k: str, v: Union[int | float]) -> tuple:
    return tuple(k, v)