#!/usr/bin/env python3
"""
This module defines a coroutine, measure_runtime, to measure the
total runtime of async_comprehension.
"""
from asyncio import gather, run
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times
    in parallel using asyncio.gather.
    Measures and returns the total runtime.
    """
    start_time = time()

    # Execute async_comprehension four times in parallel
    await gather(*(async_comprehension() for _ in range(4)))

    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
