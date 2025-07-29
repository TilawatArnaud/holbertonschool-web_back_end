#!/usr/bin/env python3
"""Measure the runtime of parallel async comprehensions."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times in parallel and measure total runtime.
    This coroutine runs 4 instances of async_comprehension concurrently
    using asyncio.gather and measures the total execution time.
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time
