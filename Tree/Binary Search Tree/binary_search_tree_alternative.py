"""
Binary Search Tree
-----------------------
Uses the abstraction of a Position


DISCLAIMER
----------
NOT TESTED

"""

class BinarySearchTree:
    
    class Position:
        def __init__(self, element):
            self._element = element
        
        def element(self):
            return self.element()
    
    def _subtree_search(self, p, k):
        if k == p.element():
            return p
        elif k < p.element():
            if self.left(p) is not None:
                return _subtree_search(self.left(p), k)
        
        else:
            if self.right(p) is not None:
                return _subtree_search(self.right(p), k)
        
        return p
    
    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        
        return walk
    
    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        
        return walk
    
    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    
    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None
    
    def inorder_predecessor(self, p):
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            parent = self.parent(walk)
            while parent is not None and walk == self.left(parent):
                walk = parent
                parent = self.parent(walk)
            
            return walk
    
    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root, k)
            self._rebalance_access(p)
            return p
    
    def find_min(self):
        if self.is_empty():
            return None
        else:
            return self.first()
    
    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.element() < k:
                p = self.after(p)
            return p
    
    def find_range(self, start=None, stop=None):
        if start is None:
            start = self.first()
        else:
            p = self.find_position(start)
            if p.element() < start:
                p = self.after(p)
        
        while p is not None and (stop is None or p.element() < stop):
            yield p.element()
            p = self.after(p)
    
    def insert(self, element):
        if self.is_empty():
            self._add_root(self.Position(node))
        else:
            p = self._subtree_search(element)
            if p.element() == element:
                p._element = element
                self._rebalance_access(p)
                return
            else:
                if p.element() < element:
                    leaf = p._add_left(p, self.Position(node))
                else:
                    leaf = p._add_right(p, self.Position(node))
        self._rebalance_access(leaf)
    
    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def delete(self, p):
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(p)