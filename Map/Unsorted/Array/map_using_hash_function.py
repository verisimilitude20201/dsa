"""
Approach
--------
Hash table using separate chaining and Multiply-Add-Divide Method.

Complexity:
Space: O(m + n): m = number of buckets, n = elements within each bucket.
Time: O(1)/O(n) in case of collisions.
"""
from random import randrange

from map import UnsortedMap


class HashMapPython:
    def __init__(self, capacity=11, p=113):
        self.n = 0
        self._table = [None] * capacity
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)
        self._prime = p

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedMap()
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        del bucket[k]

    def _hash_function(self, k):
        return (((hash(k) * self._scale) + self._shift) % self._prime) % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self.resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items)
        self._table = c * [None]
        for (k, v) in old:
            self._table[k] = v

