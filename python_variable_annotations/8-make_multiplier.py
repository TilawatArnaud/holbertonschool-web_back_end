#!/usr/bin/env python3
"""This module define a function to make a multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float number."""
    return lambda x: x * multiplier
