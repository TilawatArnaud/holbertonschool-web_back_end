#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """Asynchronous coroutine that waits for a random delay
    between 0 and max_delay.

    Args:
        n (int): Number of times to wait.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[asyncio.Task]: List of tasks.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return asyncio.as_completed(tasks)
