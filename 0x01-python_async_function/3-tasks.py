#!/usr/bin/env python3
"""
Returns a asyncio.Task obj

Modules imported: asyncio

asyncio:
    api module for IO operations using async concurrency
random:
    generate random ints
wait_random:
    calls several coroutines

"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio task obj"""
    task = asyncio.create_task(wait_random(max_delay))

    return task
