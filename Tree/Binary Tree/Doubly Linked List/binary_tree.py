import json
import jsonpickle

"""
Binary Tree using a doubly linked list.
--------------------------------------
Here we return after creating each node. Also, we're maintaining the pointer for each node that makes it easy to traverse the tree
efficiently.

Complexity
---------
1. Time: O(1) for all methods except depth and height. For depth & height & traversals, its O(N) worst case.
2. O(N): Space complexity where N is the number of nodes.

"""


class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    class Node:
        def __init__(self, data):
            self._left = None
            self._right = None
            self._parent = None
            self._data = data

    def root(self, element):
        if self._root is None:
            node = self.Node(element)
            self._root = node
        else:
            raise Exception("Root node already exists!!")

        return self._root

    def insert_left(self, node, element):
        if node._left is not None:
            raise Exception("Current node already has a left child")
        new_node = self.Node(element)
        node._left = new_node
        new_node._parent = node
        self._increment_size()

        return new_node

    def insert_right(self, node, element):
        if node._right is not None:
            raise Exception("Current node already has a right child")
        new_node = self.Node(element)
        node._right = new_node
        new_node._parent = node
        self._increment_size()

        return new_node

    def _increment_size(self):
        self._size += 1

    def is_root(self, p):
        return self._root is p

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(p._parent)

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))

    def children(self, p):
        if p._left is not None:
            yield p._left

        if p._right is not None:
            yield p._right

    def is_leaf(self, p):
        return p._left is None and p._right is None

    def preorder_traversal(self, node):
        print(node._data, sep="", end=" ")
        if node._left is not None:
            self.preorder_traversal(node._left)

        if node._right is not None:
            self.preorder_traversal(node._right)

    def postorder_traversal(self, node):
        if node._left is not None:
            self.postorder_traversal(node._left)

        if node._right is not None:
            self.postorder_traversal(node._right)

        print(node._data, sep="", end=" ")

    def inorder_traversal(self, node):
        if node._left is not None:
            self.inorder_traversal(node._left)

        print(node._data, sep="", end=" ")

        if node._right is not None:
            self.inorder_traversal(node._right)


bt = BinaryTree()
root = bt.root(10)
nodeL1 = bt.insert_left(root, 18)
nodeR1 = bt.insert_right(root, 22)
print(bt.depth(nodeR1))
nodeLL1 = bt.insert_left(nodeL1, 23)
nodeRL1 = bt.insert_right(nodeL1, 5)
print(bt.depth(nodeRL1))
nodeRL1 = bt.insert_left(nodeR1, 17)
nodeRR1 = bt.insert_right(nodeR1, 25)
print(bt.height(root))
bt.preorder_traversal(root)
print("\n")
bt.postorder_traversal(root)
print("\n")
bt.inorder_traversal(root)
serialized = jsonpickle.encode(bt)
print(json.dumps(json.loads(serialized), indent=2))
