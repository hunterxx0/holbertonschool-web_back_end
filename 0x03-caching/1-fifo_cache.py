#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ a caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > BaseCaching.MAX_ITEMS:
                popped = list(self.cache_data.keys())[0]
                print("DISCARD: " + popped)
                self.cache_data.pop(popped)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
