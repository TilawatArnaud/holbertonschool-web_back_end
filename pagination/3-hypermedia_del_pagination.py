#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination metadata for
        deletion-resilient pagination.

        Args:
            index: Start index of the return page (0-indexed)
            page_size: Number of items per page

        Returns:
            Dictionary containing:
            - index: current start index of the return page
            - next_index: next index to query with
            - page_size: current page size
            - data: actual page of the dataset
        """
        assert isinstance(index, int) and index >= 0, \
            "index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        indexed_dataset = self.indexed_dataset()
        data = []
        current_index = index
        remaining_items = page_size

        # Collect data items until we have enough or reach the end
        max_index = max(indexed_dataset.keys()) + 1 if indexed_dataset else 0
        while remaining_items > 0 and current_index < max_index:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                remaining_items -= 1
            current_index += 1

        # Find next index (first index after last item in current page)
        next_index = current_index
        while next_index in indexed_dataset and len(data) < page_size:
            next_index += 1

        return {
            'index': index,
            'next_index': next_index if data else index,
            'page_size': len(data),
            'data': data
        }
