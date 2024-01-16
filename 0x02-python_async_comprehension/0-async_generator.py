#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine, async_generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator coroutine that yields a random number between 0 and 10
    after waiting asynchronously for 1 second. This process repeats 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
