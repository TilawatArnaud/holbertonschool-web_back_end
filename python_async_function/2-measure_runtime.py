#!/usr/bin/env python3
"""
    This module provides a function to measure the average
    execution time of the wait_n coroutine.
"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): Number of times to run wait_n.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time taken per operation.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
