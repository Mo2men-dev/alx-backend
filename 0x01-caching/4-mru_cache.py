#!/usr/bin/env python3
"""
MRU implementation of caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRC caching class
    """
    def __init__(self):
        """
        inits the class
        """
        super().__init__()
        self.mru_key = ""

    def put(self, key, item):
        """
        sets an item following the MRU rule
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            del self.cache_data[self.mru_key]
            print(f"DISCARD: {self.mru_key}")

        self.mru_key = key
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item based on key
        """

        if key is not None and key in list(self.cache_data.keys()):
            self.mru_key = key
            return self.cache_data[key]

        return None
