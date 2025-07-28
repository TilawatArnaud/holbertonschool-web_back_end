#!/usr/bin/env python3
"""This module define a function to return the length of a list."""
from typing import List, Tuple


def element_length(lst: List) -> List[Tuple]:
    """Return the length of a list."""
    return [(x, len(x)) for x in lst]
