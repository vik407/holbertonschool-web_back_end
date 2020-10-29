#!/usr/bin/env python3
""" 2. Hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10):
        """ Finds the correct indexes to paginate dataset.
        """
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        end = min(end, len(self.dataset()))
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """ Returns a dictionary.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)
