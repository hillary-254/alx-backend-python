#!/usr/bin/env python3
"""
Module documentation for 0-basic_async_syntax.py
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine waiting for random delay between 0 max_delay seconds

    :param max_delay: The maximum delay in seconds (default is 10).
    :type max_delay: int
    :return: The random delay.
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
