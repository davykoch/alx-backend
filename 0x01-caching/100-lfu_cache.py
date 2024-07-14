#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.lru = defaultdict(OrderedDict)
        self.min_frequency = 0

    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: The key to add
            item: The value to associate with the key

        Returns:
            None
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                # Find the LFU item(s)
                lfu_items = self.lru[self.min_frequency]
                lfu_key, _ = lfu_items.popitem(last=False)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                if not lfu_items:
                    del self.lru[self.min_frequency]
                print(f"DISCARD: {lfu_key}")

            # Update cache
            self.cache_data[key] = item
            self._update_frequency(key)

    def get(self, key):
        """
        Get an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        if key is not None and key in self.cache_data:
            self._update_frequency(key)
            return self.cache_data[key]
        return None

    def _update_frequency(self, key):
        """
        Update the frequency of an item

        Args:
            key: The key to update
        """
        freq = self.frequency[key]
        self.frequency[key] += 1
        if freq > 0:
            del self.lru[freq][key]
            if not self.lru[freq]:
                del self.lru[freq]
                if freq == self.min_frequency:
                    self.min_frequency += 1
        else:
            self.min_frequency = 1
        self.lru[self.frequency[key]][key] = None
