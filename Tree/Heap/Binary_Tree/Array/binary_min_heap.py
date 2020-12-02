"""
Approach
--------
1. MinHeap that organizes elements using an Array representation of a binary Tree
2. For a position p, if its a root, the values of its descendants are in a non-decreasing order.
3. The minimum element is that at the root.
4. Has two properties 
    i. Heap order property: Parent element is less than the value of the element of its children
    ii. Complete binary Tree: Each level of the tree has 2^i nodes where i goes from 0 to h - 1, h being the height of the node.]

5. Can be used as a Priority Queue..

Complexity
---------
1. Time: O(Log N) for insertion and deletion
2. Time: O(1) for finding the minimum element.
3. Time: O(log h) for doing the swaps.

"""
class MinHeap:

    def __init__(self):
        self._data = []

    class Item:
        def __init__(self, priority, value):
            self._priority = priority
            self._value = value

        def __lt__(self, other):
            return self._priority < other._priority

    def add_item(self, priority, value):
        item = self.Item(priority, value)
        self._data.append(item)
        self._up_heap(len(self._data) - 1)



    def find_min(self):
        if len(self._data) == 0:
            raise Exception("Empty Min heap, add more data")
        item = self._data[0]

        return item._priority, item._value

    def remove_min(self):
        if len(self._data) == 0:
            raise Exception("Min heap is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._down_heap(0)

        return item._priority, item._value

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _up_heap(self, i):
        parent = self._parent(i)
        while i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._up_heap(parent)

    def _down_heap(self, i):
        smallest_element = None
        if self._has_left(i):
            left_child = self._left(i)
            smallest_element = left_child
            if self._has_right(i):
                right_child = self._right(i)
                if self._data[right_child] < self._data[left_child]:
                    smallest_element = right_child

            if self._data[i] > self._data[smallest_element]:
                self._swap(i, smallest_element)
                self._down_heap(smallest_element)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)