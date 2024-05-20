#!/usr/bin/env python3
"""Returns a tuple of size two pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index ranges"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
