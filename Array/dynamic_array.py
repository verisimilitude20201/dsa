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

    def _make_array(c):
        return (c * ctypes.py_object)()