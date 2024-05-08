#!/usr/bin/env python3
"""
task1.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """init..
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)
        else:
            return

    def get(self, key):
        """
        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.cache_data.get(key, None)
