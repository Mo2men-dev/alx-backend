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

        print(f"current list: {self.lru_list}")

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.lru_list.pop()
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.lru_list.insert(0, key)
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item by key from cache
        """
        print(f"current list: {self.lru_list}")
        if key in self.lru_list:
            indx = self.lru_list.index(key)
            k = self.lru_list[indx]
            del self.lru_list[indx]
        if key is not None and key in list(self.cache_data.keys()):
            self.lru_list.insert(0, key)
            return self.cache_data[key]

        return None
