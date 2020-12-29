"""
Simple Trie

Complexity
---------
Space: O(Length of the longest word)
Time: O(N^2) N is the length of the longest word and it may have N children

"""
from typing import Tuple


class Trienode:

    def __init__(self):
        self._root = None

    class Node:
        def __init__(self, char: str):
            self._char = char
            self._counter = 1
            self._children = []

        def get_children(self):
            return self._children

        def get_char(self):
            return self._char

        def get_counter(self):
            return self._counter

        def inc_counter(self):
            self._counter += 1

        def append_children(self, node):
            self._children.append(node)

    def add(self, word : str) -> Tuple[bool, int]:
        if self._root is None:
            self._root = self.Node("*")

        node = self._root
        for character in word:
            found_in_child = False
            for child in node.get_children():
                if child.get_char() == character:
                    child.inc_counter()
                    node = child
                    found_in_child = True
                    break

            if not found_in_child:
                new_node = self.Node(character)
                node.append_children(new_node)
                node = new_node
                node.inc_counter()

    def find_prefix(self, prefix):
        node = self._root
        if not node.get_children():
            return False, 0

        for char in prefix:
            char_not_found = False
            for child in node.get_children():
                if child.get_char() == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0

        return True, node.get_counter()

trie = Trienode()
trie.add("hackathon")
trie.add('hack')

print(trie.find_prefix('hac'))
print(trie.find_prefix('hackatho'))