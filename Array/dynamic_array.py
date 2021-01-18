"""
Problem:
--------
Dynamic array implementation in Python

Complexity
----------
Space: O(N)
Time:
    __len__ -> O(1)
    __resize__ -> O(capacity)
    __append__ -> O(1) amortized / O(N) worst case
    __getitem__ --> O(1)
    __setitem__ --> O(1)
    __delitem__ --> O(1)
    
"""

import ctypes


class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._N = 0
        self._A = self._make_array(self._capacity)

    def append(self, object):
        if self._N == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._N] = object
        self._N += 1

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for i in range(len(self._A)):
            B[i] = self._A[i]
        self._A = B
        self._capacity = capacity

    def __len__(self):
        return self._N

    def __getitem__(self, index):
        return self._A[index]

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __delitem__(self, key):
        self._A[key] = None
        if len(self) <= self._capacity // 2:
            self._resize(self._capacity // 2)

        self._N -= 1

da = DynamicArray()
da.append(1)
da.append(2)
da.append(3)
da.append(4)
print(da.__getitem__(3))
print(len(da))
del da[3]
del da[2]
print(len(da))
print(da.__getitem__(3))
