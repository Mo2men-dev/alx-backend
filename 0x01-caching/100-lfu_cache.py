#!/usr/bin/env python3
"""
LFU implementation of caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching class
    """

    def __init__(self):
        """
        inits the class
        """
        super().__init__()
        self.lru_list = []
        self.lfu_dic = {}

    def put(self, key, item):
        """
        sets item using the LFU policy
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            minm = min(list(self.lfu_dic.items()))[1]
            lfu_keys = [k for k, v in self.lfu_dic.items() if v == minm]
            deleted_key = ''

            if len(lfu_keys) == 1:
                deleted_key = lfu_keys[0]
            else:
                indx = max([self.lru_list.index(k) for k in lfu_keys])
                deleted_key = self.lru_list[indx]

            del self.lfu_dic[deleted_key]
            del self.lru_list[self.lru_list.index(deleted_key)]
            del self.cache_data[deleted_key]

            print(f"DISCARD: {deleted_key}")

        self.lru_list.insert(0, key)
        self.cache_data[key] = item

        if key in self.lfu_dic.keys():
            self.lfu_dic[key] += 1
        else:
            self.lfu_dic[key] = 1

    def get(self, key):
        """
        get item from key
        """

        if key in self.lru_list:
            indx = self.lru_list.index(key)
            k = self.lru_list[indx]
            del self.lru_list[indx]

        if key is not None and key in list(self.cache_data.keys()):
            if key in self.lfu_dic.keys():
                self.lfu_dic[key] += 1
            else:
                self.lfu_dic[key] = 1

            self.lru_list.insert(0, key)
            return self.cache_data[key]

        return None
