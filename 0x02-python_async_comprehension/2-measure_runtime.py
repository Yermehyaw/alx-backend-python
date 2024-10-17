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
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:   
    """
    Measures runtime

    Returns:
    A float rep time elasped
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_generator(),
        async_generator(),
        async_generator(),
        async_generator()
    )
    end = time.perf_counter()
    return (end - start)
