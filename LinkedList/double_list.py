class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def prepend(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._increment_length()

    def append(self, data):
        new_node = self.Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._increment_length()

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
        elif index <= 0:
            self.prepend(value)
        else:
            current_node = self._traverse_nodes_till(index)
            new_node = self.Node(value)
            old_prev_node = current_node.prev
            old_prev_node.next = new_node
            new_node.prev = old_prev_node
            new_node.next = current_node
            current_node.prev = new_node
        self._increment_length()

    def remove(self, index):
        if index <= 0:
            self.head = self.head.next
            self.head.prev = None
        elif index >= self.length:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self._traverse_nodes_till(index)
            new_previous_node = current_node.prev
            new_next_node = current_node.next
            new_previous_node.next = new_next_node
            new_next_node.prev = new_previous_node
        self._decrement_length()

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, sep="", end=" <--> ")
            current_node = current_node.next

    def _traverse_nodes_till(self, index):
        current_node = self.head
        current_index = 0
        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def _increment_length(self):
        self.length += 1

    def _decrement_length(self):
        self.length -= 1


if __name__ == '__main__':
    dlist = DoubleLinkedList()
    dlist.prepend(0)
    dlist.prepend(-1)
    dlist.prepend(-2)
    dlist.prepend(-3)
    dlist.prepend(-4)
    dlist.prepend(-5)
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    dlist.append(4)
    dlist.append(5)
    dlist.insert(1, -4.5)
    dlist.remove(1)
    dlist.remove(0)
    dlist.print_list()
