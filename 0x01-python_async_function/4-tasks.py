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
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> list:
    """Return a list of elasped times in calling each coroutine"""
    cor_delays = []

    for i in range(n):
        d_n = task_wait_random(max_delay)
        delays.append(d_n)

    return cor_delays
