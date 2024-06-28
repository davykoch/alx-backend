#!/usr/bin/env python3
"""This module contains a Server class to paginate a database
of popular baby names."""

import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> tuple:
    """Calculate start and end indices for pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data."""
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer")
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer")

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data with hypermedia pagination metadata.

        Args:
        - page (int): The page number (1-indexed). Defaults to 1.
        - page_size (int): The number of items per page. Defaults to 10.

        Returns:
        - Dict: A dictionary containing pagination metadata and data.
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
