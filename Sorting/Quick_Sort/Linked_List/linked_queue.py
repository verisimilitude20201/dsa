class LinkedQueue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._n = 0

    def __len__(self):
        return self._n

    def enqueue(self, data):
        new_node = self.Node(data)
        if self._tail is None:
            self._tail = new_node
            self._head = self._tail
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        first_node = self._head

        self._head = self._head.next
        self._n -= 1
        if self.is_empty():
            self._tail = None
        return first_node.data

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self._head.data

    def is_empty(self):
        return self._n == 0
