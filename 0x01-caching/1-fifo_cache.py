#!/usr/bin/env python3
"""
FIFO implementation of caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO class for caching
    """

    def __init__(self):
        """
        inits the class
        """
        super().__init__()

    def put(self, key, item):
        """
        puts in an item following the FIFO policy
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        gets item by key from cache
        """

        return self.cache_data.get(key, None)
