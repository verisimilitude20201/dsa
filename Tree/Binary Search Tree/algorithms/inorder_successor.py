"""
Problem
------
Find the in-order successor of a node in a Binary search tree

1. If p has a right sub-tree, its in order sucessor is the left most node of the right-subtree
2. If p does not have a right sub-tree, its in order successor is the ancestor that contains p in its left subtree

Complexity
----------
Time: O(h) where h is the height of the Tree.
Space: O(1)

Note: This is a plain algorithm
"""

def inorder_successor(p):
    if p.right() is not None:
        walk = p.right()
        while walk.left() is not None:
            walk = walk.left()
        return walk
    else:
        walk = p
        ancestor = parent(walk)
        while ancestor is not None and walk == ancestor.right():
            walk = ancestor
            ancestor = parent(walk)
        
        return walk