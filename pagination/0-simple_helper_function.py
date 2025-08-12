#!/usr/bin/env python3
"""This module define a function to return a tuple of start and end index."""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of start and end index for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
