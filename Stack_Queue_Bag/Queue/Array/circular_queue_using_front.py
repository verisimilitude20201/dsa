"""
Circular Queue using just front.

Complexity:
----------

Time: 
    is_empty(), first() --> O(1)
    enqueue(), dequeue() --> O(1) amortized
    resize() --> O(MAX_CAPACITY)

Space:
    O(MAX_CAPACITY)

"""
class ArrayQueueUsingFront:
    MAX_CAPACITY = 5

    def __init__(self):
        self._data = [None] * ArrayQueueUsingFront.MAX_CAPACITY
        self._front = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def enqueue(self, value):
        if self._size == ArrayQueueUsingFront.MAX_CAPACITY:
            self.resize(2 * ArrayQueueUsingFront.MAX_CAPACITY)
        avail = (self._front + self._size) % ArrayQueueUsingFront.MAX_CAPACITY
        self._data[avail] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % ArrayQueueUsingFront.MAX_CAPACITY
        self._size -= 1

        return value

    def resize(self, capacity):
        old = self._data
        old_front = self._front
        self._data = [None] * capacity
        for i in range(self._size):
            self._data[i] = old[old_front]
            old_front = (old_front + 1) % ArrayQueueUsingFront.MAX_CAPACITY

        ArrayQueueUsingFront.MAX_CAPACITY = len(self._data)
        self._front = 0

aq = ArrayQueueUsingFront()
aq.enqueue(1)
aq.enqueue(2)
aq.enqueue(3)
aq.enqueue(5)
aq.enqueue(4)
print(aq.dequeue())
print(aq.dequeue())
aq.enqueue(6)
aq.enqueue(7)
print(aq.dequeue())