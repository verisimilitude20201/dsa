"""
Approach
--------
Hash table using linear probing and Multiply-Add-Divide Method.

Complexity:
Space: O(m) - m is the number of buckets
Time: O(1)/O(n) in case of collisions.
"""
from map_using_hash_function import HashMapPython

class LinearProbeHashMap(HashMapPython):
    _AVAIL = "AVAIL"

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] == LinearProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        first_avail = None
        while True:
            if self._is_available(j):
                first_avail = j
            if self._table[j] is None:
                return False, first_avail
            elif k == self._table[j]._key:
                return True, j
            j = (j + 1) % len(self.table)

    def _bucket_setitem(self, j, k, v):
        found, slot = self._find_slot(j, k)
        if not found:
            self._table[slot] = self.Item(k, v)
            self._n += 1
        else:
            self._table[slot]._value = v

    def _bucket_getitem(self, j, k):
        found, slot = self._find_slot(i, k)
        if not found:
            raise KeyError("Not found bucket %d or key %d" %(j, k))
        return self._table[slot]._value

    def _bucket_delitem(self, j, k):
        found, slot = self._find_slot(j, k)
        if not found:
            raise KeyError("Not found bucket %d or key %d" %(j, k))
        self._table[slot] = LinearProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key