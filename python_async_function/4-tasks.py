#!/usr/bin/env python3
"""
    This module provides a function to create and manage
    multiple asynchronous tasks that wait for random delays.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
