#!/usr/bin/env python3
"""
module for class BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache
    """

    def put(self, key, item):
        """
        sets and key with item value
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item by key
        """
        return self.cache_data.get(key, None)
