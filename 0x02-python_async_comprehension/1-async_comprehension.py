#!/usr/bin/env python3
"""
This module defines an async comprehension coroutine, async_comprehension
"""
from typing import List
from random import uniform
from asyncio import gather


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async coroutine that collects 10 random numbers using async_generator
    """
    return [i async for i in async_generator()]
