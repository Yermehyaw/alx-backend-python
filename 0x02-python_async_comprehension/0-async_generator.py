#!/usr/bin/env python3
"""
An async generator func

Modules imported:
asyncio: use asunc operation in python
random: generate random values
typing: custom types for python annotation

"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An async geb func, yields a random number

    yields:
    A random float between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
