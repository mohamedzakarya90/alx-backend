#!/usr/bin/env python3
""" The pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Retrieving index range from given page and page size
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
