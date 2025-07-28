#!/usr/bin/env python3
"""
This module provides a function to compute the length
of elements in an iterable of sequences.
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element
    and its length from the given iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence objects.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
