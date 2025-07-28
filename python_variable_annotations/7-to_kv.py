#!/usr/bin/env python3
"""This module define a function to convert
 a string and a float number to a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and a float number."""
    return (k, v * v)
