#!/usr/bin/env python3
"""
Async Comprehension
"""
from typing import List

# Import the async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10
    """
    return [i async for i in async_generator()]
