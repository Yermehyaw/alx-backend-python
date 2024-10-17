#!/usr/bin/env python3
"""
Measures the runtime of an asynchronous list comp

Modules imported:
asyncio: use async operation in python
random: generate random values
typing: custom types for python annotation

"""
import asyncio
import random
import time
a_compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime

    Returns:
    A float rep time elasped
    """
    start = time.perf_counter()
    values = await asyncio.gather(a_compr(), a_compr(), a_compr(), a_compr())
    end = time.perf_counter()
    return (end - start)
