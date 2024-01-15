#!/usr/bin/env python3
"""
Module documentation for 4-tasks.py
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine spawns task_wait_random n times with the specified max_delay

    :param n: The number of times to spawn task_wait_random.
    :type n: int
    :param max_delay: The maximum delay in seconds.
    :type max_delay: int
    :return: List of delays (float values) in ascending order.
    :rtype: List[float]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
