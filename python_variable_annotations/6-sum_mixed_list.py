#!/usr/bin/env python3
"""This module define a function to sum a list of float and int numbers."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of float and int numbers."""
    return sum(mxd_lst)
