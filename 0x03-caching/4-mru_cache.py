#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ a caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                popped = self.keys[BaseCaching.MAX_ITEMS - 1]
                print("DISCARD: " + popped)
                self.cache_data.pop(popped)
                self.keys.remove(popped)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
