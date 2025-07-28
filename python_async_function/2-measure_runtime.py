#usr/bin/env python3
"""
    This module provides an asynchronous coroutine that measures the runtime of
    multiple wait_random coroutines.
"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_runtime(n: int, max_delay: int) -> float:
    """Asynchronous coroutine that measures the runtime of multiple wait_random coroutines.

    Args:
        n (int): Number of times to wait.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: The total runtime of the wait_random coroutines.
    """
    tasks = [wait_n(max_delay) for _ in range(n)]
    return sum(await asyncio.gather(*tasks))
