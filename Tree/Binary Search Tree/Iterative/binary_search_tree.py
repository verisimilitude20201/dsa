import json
import jsonpickle

"""
Iterative Approach - BST
-----------------------

Complexity
----------
1. O(log N) Time: Amortized. Assuming that the BST is balanced
2. O(N): Space complexity
"""


class BinarySearchTree:
    def __init__(self):
        self._root = None

    class Node:
        def __init__(self, data):
            self._left = None
            self._right = None
            self._data = data

    def insert(self, value):
        new_node = self.Node(value)
        if self._root is None:
            self._root = new_node
        else:
            current_node = self._root
            while True:
                if value < current_node._data:
                    if current_node._left is None:
                        current_node._left = new_node
                        break
                    current_node = current_node._left
                else:
                    if current_node._right is None:
                        current_node._right = new_node
                        break
                    current_node = current_node._right

    def lookup(self, value):
        if self._root is None:
            return None
        else:
            current_node = self._root
            while current_node:
                if value < current_node._data:
                    current_node = current_node._left
                elif value > current_node._data:
                    current_node = current_node._right
                else:
                    return current_node
        return None

    def remove(self, value):
        current_node, prev_node = self._lookup_and_return_prev_and_current_node_for(value)
        # Delete leaf node
        if self._is_leaf_node(current_node):
            self._delete_leaf_node_and_make_previous_as_leaf(prev_node, current_node)
        # Delete node with single left child
        elif self._is_node_with_single_left_child(current_node):
            current_node = current_node._left
            self._change_prev_node_to_node_after_current(self, prev_node, current_node)
        # Delete node with single right child
        elif self._is_node_with_single_right_child(current_node):
            current_node = current_node._right
            self._change_prev_node_to_node_after_current(self, prev_node, current_node)
        # Delete node with two-children
        else:
            inorder_sucessor_node, prev_inorder_sucessor_node = self._lookup_prev_node_and_smallest_node_in_right_subtree(current_node)
            current_node._data = inorder_sucessor_node._data
            self._delete_leaf_node_and_make_previous_as_leaf(prev_inorder_sucessor_node, inorder_sucessor_node)

    def _lookup_and_return_prev_and_current_node_for(self, value):
        current_node = self._root
        prev_node = None
        while current_node:
            if value < current_node._data:
                prev_node = current_node
                current_node = current_node._left
            elif value > current_node._data:
                prev_node = current_node
                current_node = current_node._right
            else:
                return current_node, prev_node

    def _is_leaf_node(self, node):
        return node._left is None and node._right is None

    def _is_node_with_single_left_child(self, node):
        return node._right is None

    def _is_node_with_single_right_child(self, node):
        return node._left is None

    def _delete_leaf_node_and_make_previous_as_leaf(self, prev_node, current_node):
        if prev_node._data > current_node._data:
            prev_node._left = None
        else:
            prev_node._right = None

    def _change_prev_node_to_node_after_current(self, prev_node, current_node):
        if prev_node._data > current_node._data:
            prev_node._left = current_node
        else:
            prev_node._right = current_node

    def _lookup_prev_node_and_smallest_node_in_right_subtree(self, current_node):
        node_previous_to_in_order_sucessor = current_node
        in_order_sucessor_node = current_node._right
        while in_order_sucessor_node._left is not None:
            node_previous_to_in_order_sucessor = in_order_sucessor_node
            in_order_sucessor_node = in_order_sucessor_node._left

        return in_order_sucessor_node, node_previous_to_in_order_sucessor


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.remove(9)
#bst.remove(1)

serialized = jsonpickle.encode(bst)
print(json.dumps(json.loads(serialized), indent=2))
