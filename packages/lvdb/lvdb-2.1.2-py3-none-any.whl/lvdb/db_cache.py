import asyncio
import collections
from typing import Optional


class DBCache(asyncio.Protocol):
    def __init__(self):
        self.__ttl = collections.defaultdict(lambda: (float('inf'), float('inf')))
        self.__cache = {}
        self.__monotonic = 0

    @property
    def cache(self):
        return self.__cache

    def set(self, key, value, queries_to_live: Optional[int] = None):
        self.__cache[key] = value
        if queries_to_live:
            self.__ttl[key] = (queries_to_live, self.__monotonic)
        else:
            self.__ttl.pop(key, None)
        self.__monotonic += 1

    def remove_if_expired(self, key):
        if key in self.__ttl and self.__ttl[key][0] <= self.__monotonic - self.__ttl[key][1]:
            del self.__cache[key]
            del self.__ttl[key]

    def get(self, key):
        self.remove_if_expired(key)
        self.__monotonic += 1
        return self.__cache.get(key, None)