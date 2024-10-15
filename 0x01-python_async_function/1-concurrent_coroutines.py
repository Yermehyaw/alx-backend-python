#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async

Modules imported: asyncio

asyncio:
    api module for IO operations using async concurrency
random:
    generate random ints
wait_random:
    wait for a random time

"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Return a list of all random return times"""
    delays = []
    for i in range(n):
        d_n = asyncio.create_task(wait_random(max_delay))
        delay = await d_n
        delays.append(delay)

    return delays
