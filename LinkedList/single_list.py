class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def prepend(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, data):
        new_node = self.Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, sep="", end=" --> ")
            current_node = current_node.next