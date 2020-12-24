"""
AVL Tree
-----------------------
AVL Tree is a BST whose difference in height at each position is less than or equal to 1. It guarantees worst-case O(log N) time
for each operation


DISCLAIMER
----------
NOT TESTED

"""

class AVLTree(BinarySearchTree):
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None)
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0
    
    def left_height(self):
        return self._left._height if self._left is not None else 0
    
    def right_height(self):
        return self._right._height if self._right is not None else 0
    
    def _recompute_height(self, p):
        p._node._height = 1 + max(p.left_height(), p.right_height())
    
    def _is_balanced(self, p):
        return abs((p.left_height() - p.right_height()) <= 1
    
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
    
    def _tall_child(self, p, favor_left=False):
        if p.left_height() + (1 if favor_left else 0) < p.right_height():
            return self.left(p)
        else:
            return self.right(p)
    
    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._is_balanced(p):
                p = self.restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)
    
    def _rebalance_delete(self, p):
        self._rebalance(p)