#!/usr/bin/env python3
"""
Forms a list via async comprehension

Modules imported:
asyncio: use async operation in python
random: generate random values
typing: custom types for python annotation

"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Produces a list from an async gen using list
    comprehension

    Returns:
    A list of floats
    """
    return [rand async for rand in async_generator()]
