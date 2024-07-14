#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded = self.order.pop(0)
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")

            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """
        Get an item by key

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key) if key is not None else None
