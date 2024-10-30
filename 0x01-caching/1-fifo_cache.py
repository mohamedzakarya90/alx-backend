#!/usr/bin/env python3

''' Task 1 -> FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' The class FIFOCache which inherits from
       BaseCaching and is caching system
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assigning to dictionary self.cache_data and the
           item value for key key
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        ''' Returning value in self.cache_data which is linked to key
        '''
        return self.cache_data.get(key, None)
