#!/usr/bin/env python3
"""
Module documentation for 3-tasks.py
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that take an integer max_delay and return an asyncio.Task

    :param max_delay: The maximum delay in seconds.
    :type max_delay: int
    :return: An asyncio.Task.
    :rtype: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
