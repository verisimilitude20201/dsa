"""
Splay Tree
-----------------------
Splay Tree is a BST on which a splay operation is applied to keep all most recently accessed nodes closer to the root of the tree


DISCLAIMER
----------
NOT TESTED

Complexity
---------
Space: O(1)
Time: O(d) where d is the depth of the position p. Worst case may go to O(h) where h is the height of the tree, given that the element can be in the deepest 
position.

"""

class SplayTree(BinarySearchTree):
    def _splay(self, p):
        while p !-= self.root():
            parent = self.parent(p)
            grandparent = self.parent(parent)
            if grandparent is None:
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)
    
    def _rebalance_insert(self, p):
        self._splay(p)
    
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)
    
    def _rebalance_access(self, p):
        self._splay(p)
