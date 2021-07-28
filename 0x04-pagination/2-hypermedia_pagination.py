#!/usr/bin/env python3
""" Hypermedia pagination module
"""
import csv
import math
from typing import List, Any, Dict
index_range = __import__('0-simple_helper_function').index_range


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the page data simple method
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        st, end = index_range(page, page_size)
        data = self.dataset()
        if st >= len(data):
            return []
        return data[st: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return the page data Hypermedia method
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        if (page + 1) < math.ceil(len(self.dataset()) / page_size):
            npage = page + 1
        else:
            npage = None
        if page > 1:
            ppage = page - 1
        else:
            ppage = None

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": npage,
            "prev_page": ppage,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
