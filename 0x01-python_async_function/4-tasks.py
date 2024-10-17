#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async with exec times
measured

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
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of elasped times in calling each coroutine"""
    # compile a list of Task objs from task_wait_random()
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Insert each completed task according to completion duration
    compl_tasks = [await task for task in asyncio.as_completed(tasks)]

    return compl_tasks
