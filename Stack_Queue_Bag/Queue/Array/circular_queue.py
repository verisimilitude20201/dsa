class CircularQueue:
    def __init__(self, initial_capacity=4):
        self._data = [None] * initial_capacity
        self._front = -1
        self._rear = -1

    def enqueue(self, element):
        if self.is_empty():
            self._front = 0
            self._rear = 0
            self._data[self._rear] = element
        elif self.is_full():
            raise Exception("Queue is full")
        else:
            self._rear = (self._rear + 1) % len(self._data)
            self._data[self._rear] = element

    def dequeue(self):
        if self._front == self._rear:
            data = self._data[self._front]
            self._front = self._rear = -1
            return data
        elif self.is_empty():
            raise Exception("Queue is empty")
        else:
            data = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)

            return data

    def is_empty(self):
        return self._front == -1 and self._rear == -1

    def is_full(self):
        return (self._rear + 1) % len(self._data) == self._front


cq = CircularQueue()
cq.enqueue(1)
cq.print_queue()
cq.enqueue(2)
cq.print_queue()
cq.enqueue(3)
cq.print_queue()
cq.enqueue(4)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
