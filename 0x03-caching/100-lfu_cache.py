#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ a caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys[key] += 1
            else:
                self.keys[key] = 0
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                popped = min(self.keys, key=self.keys.get)
                if popped == key:
                    self.keys.pop(popped)
                    popped = min(self.keys, key=self.keys.get)
                    self.keys[key] = 0
                print("DISCARD: " + popped)
                self.cache_data.pop(popped)
                self.keys.pop(popped)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.keys[key] += 1
            return self.cache_data[key]
        return None
