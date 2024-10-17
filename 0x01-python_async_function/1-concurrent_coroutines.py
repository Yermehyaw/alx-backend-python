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
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of all random return times"""
    delays = []
    task_objs = []

    for _ in range(n):
        task_objs.append(asyncio.create_task(wait_random(max_delay)))

    try:
        delays = [await finsh for finsh in asyncio.as_completed(task_objs)]
    except Exception as e:
        print(f'Async event loop was unexpectedly interrupted: {e}')
        # a graceful event loop closure is also supppsed to be here.

    return delays
