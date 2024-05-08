#!/usr/bin/env python3
"""task1"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache BaseCaching"""
    def __init__(self):
        """ init.."""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """function add item"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)
        else:
            return

    def get(self, key):
        """ get item """
        return self.cache_data.get(key, None)
