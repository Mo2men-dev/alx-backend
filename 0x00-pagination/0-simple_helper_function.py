#!/usr/bin/env python3
"""
module with helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Simple helper function
    """
    start = page_size * (page - 1)
    return (start, start + page_size)
