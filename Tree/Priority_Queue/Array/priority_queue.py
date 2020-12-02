"""
Priority Queue using an Array

Complexity
-------------
Time: O(N^2) to Cater for finding the min and removing it
Space: O(N)
"""
class PriorityQueue:

    def __init__(self):
        self._data = []

    class Item:
        def __init__(self, priority, value):
            self._priority = priority
            self._value = value

    def add_item(self, priority, value):
        item = self.Item(priority, value)
        self._data.append(item)

    def _find_min(self):
        first_item = self._data[0]
        first_index = 0
        for index in range(1, len(self._data)):
            item = self._data[index]
            if item._priority < first_item._priority:
                first_item = item
                first_index = index

        return first_index, first_item

    def remove(self):
        first_index, first_item = self._find_min()
        del self._data[first_index]

        return first_item


pq = PriorityQueue()
pq.add_item(0, 1000)
pq.add_item(1, 1002)
pq.add_item(2, 1003)
print(pq.remove())
print(pq.remove())
print(pq.remove())
