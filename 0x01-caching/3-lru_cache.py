#!/usr/bin/env python3
"""
LRU implementation of caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching class
    """

    def __init__(self):
        """
        inits the class
        """
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """
        sets item using the LRU policy
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.lru_list[-1]
            del self.cache_data[lru_key]
            self.lru_list.pop()
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """
        gets item by key from cache
        """
        if key is not None and key in list(self.cache_data.keys()):
            self.lru_list.append(key)
            return self.cache_data[key]

        return None
