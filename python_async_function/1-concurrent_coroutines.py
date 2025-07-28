#!/usr/bin/env python3
"""
    This module provides an asynchronous coroutine
    that waits for a random delay. It also includes
    a function to run multiple wait_random coroutines
    concurrently.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that waits for a random delay
    between 0 and max_delay.

    Args:
        n (int): Number of times to wait.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of random delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
