#!/usr/bin/env python3
"""Implements the caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class creation of a caching system"""
    def put(self, key, item):
        """Puts the item in the caching system"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get the cached item"""
        return self.cache_data.get(key, None)
