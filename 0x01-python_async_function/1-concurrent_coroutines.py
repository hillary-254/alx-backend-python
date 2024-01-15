#!/usr/bin/env python3
"""
Module documentation for 1-concurrent_coroutines.py
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine spawns wait_random n times with specified max_delay

    :param n: The number of times to spawn wait_random.
    :type n: int
    :param max_delay: The maximum delay in seconds.
    :type max_delay: int
    :return: List of delays (float values) in ascending order.
    :rtype: List[float]
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
