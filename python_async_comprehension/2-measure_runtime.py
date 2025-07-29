#!/usr/bin/env python3
"""
Measure Runtime
"""
import asyncio
import time

# Import the async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.
    
    Returns:
        float: Total runtime in seconds
    """
    start_time = time.time()
    
    # Run four async_comprehension coroutines in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.time()
    return end_time - start_time
