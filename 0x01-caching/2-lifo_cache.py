#!/usr/bin/env python3
"""
LIFO implementation of caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO class for caching
    """

    def __init__(self):
        """
        inits the class
        """
        super().__init__()

    def put(self, key, item):
        """
        sets an item follwing the LIFO policy
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        gets item by key from cache
        """

        return self.cache_data.get(key, None)
