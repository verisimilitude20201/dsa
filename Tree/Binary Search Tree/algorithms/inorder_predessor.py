"""
Problem
------
Find the in-order predecessor of a node in a Binary search tree

1. If p has a left sub-tree, its in order predecessor is the right most node of the left subtree
2. If p does not have a left sub-tree, its in order predecessor is the ancestor that contains p in its right subtree

Complexity
----------
Time: O(h) where h is the height of the Tree.
Space: O(1)

Note: This is a plain algorithm

"""


def inorder_predecessor(p):
    if p.left() is not None:
        walk = p.left()
        while walk.right() is not None:
            walk = walk.right()
        return walk
    else:
        walk = p
        ancestor = parent(walk)
        while ancestor is not None and walk == ancestor.left():
            walk = ancestor
            ancestor = parent(walk)
        
        return walk