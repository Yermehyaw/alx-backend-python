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


async def wait_n() -> list:
