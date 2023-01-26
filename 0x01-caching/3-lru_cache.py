#!/usr/bin/python3
""" 3. LRU Caching """

from datetime import datetime

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.obj = {}

    def put(self, key, item):
        """  assign to the dictionary self.cache_data the item value for
        the key key """
        if key and item:
            if key in self.obj:
                del self.obj[key]
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lru_time = min(self.obj.values())
                for k in self.obj.keys():
                    if self.obj[k] == lru_time:
                        del self.obj[k]
                        del self.cache_data[k]
                        print("DISCARD: {}".format(k))
                        break
            self.obj[key] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
