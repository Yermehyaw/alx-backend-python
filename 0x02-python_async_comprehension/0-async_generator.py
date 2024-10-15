#!/usr/binnv python3
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


async def async_generator() -> Generator[int, None, None]:
    """An async geb func, yields a random number"""
    for _ in range(10):
        await ayncio.sleep(1)
        rand = random.unifirm(0, 10)
        yield rand