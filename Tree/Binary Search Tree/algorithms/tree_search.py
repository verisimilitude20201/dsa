"""
Problem
------
Check whether a given key exists in a BST

1. If the key is equal to the searched key, return the position
2. If the key is less than searched key and there is a left subtree, recursively call the function again, passing in the left sub-tree
3. If the key is greater than searched key and there is a right subtree, recursively call the function again, passing in the right sub-tree

Complexity
----------
Time: O(h) where h is the height of the Tree.
Space: O(h)

Note: This is a plain algorithm

"""
def tree_search(key):
    def search_bst(p, key)
        if p.key() == key:
            return p
        
        if p.left() is not None and p.key() < key:
            return search_bst(p.left, key)
        
        if p.right() is not None and p.key > key
            return search_bst(p.right, key)
        
        return p

    return search_bst(root, key)    
    
    