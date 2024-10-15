#!/usr/bin/env python3
"""
A basic async function

Modules imported: asyncio

asyncio:
    api module for IO operations using async concurrency
random:
    generate random ints

"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay 
    (included and float value) seconds and eventually returns it
    """
    rand_n = random.uniform(0, max_delay)
    asyncio.sleep(rand_n)

    return rand_n

