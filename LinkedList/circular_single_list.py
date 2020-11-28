"""
Approach
---------
Code is similar to that of a singly linked list, the only difference is to account for the tail's next pointing back to head.

"""
class CircularLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None

    def prepend(self, element):
        new_node = self.Node(element)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
        else:
            new_node._next = self._head
            self._head = new_node
            self._tail._next = self._head

    def append(self, element):
        new_node = self.Node(element)
        if self._tail is None:
            self._tail = new_node
            self._head = self._tail
        else:
            self._tail._next = new_node
            self._tail = new_node
            self._tail._next = self._head

    


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
