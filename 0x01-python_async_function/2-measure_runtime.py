#!/usr/bin/env python3
"""
Measure the runtime of multiple coroutines

Modules imported: asyncio

asyncio:
    api module for IO operations using async concurrency
random:
    generate random ints
time:
    provides chronlogical interfaces
wait_n:
    runs multiple coroutines

"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures execution time per coroutine awaited in the wait_n() func"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    elasped = end - start

    return elasped/n
