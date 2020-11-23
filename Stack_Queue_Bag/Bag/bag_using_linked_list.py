"""
Concept
-------
1. Similar to a Stack. Only has add method.
2. Not allowed to remove elements from the Bag.

Time-Complexity
--------------



"""
class Bag:
    first = None
    N = 0
    last = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        return self.first is None

    def add(self, data):
        old_first = self.first
        self.first = self.Node(data)
        if old_first:
            self.first.next = old_first

    def traverse(self):
        bag_items = ""
        while self.first:
            bag_items += str(self.first.data) + " -> "
            self.first = self.first.next
        bag_items += "NULL"

        return bag_items

    def get_size(self):
        return self.N


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    bag = Bag()
    for loop_ctr in range(0, len(A)):
        bag.add(A[loop_ctr])

    print(bag.traverse())






