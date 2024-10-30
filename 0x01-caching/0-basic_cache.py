#!/usr/bin/env python3

''' Task 0 -> Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' The class BasicCache which inherits from BaseCaching
        and is caching system
    '''

    def put(self, key, item):
        ''' Assigning to dictionary self.cache_data 
            and the item  value for the key key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returning value in self.cache_data which is linked to key
        '''

        return self.cache_data.get(key, None)
