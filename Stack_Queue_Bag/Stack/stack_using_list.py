"""
Stack that uses an underlying list for implementation (Adapter Pattern)
Time/Space complexity for all operations O(1) / O(1)
"""


class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self._is_empty():
            raise Exception("Stack is empty!")
        return self._data.pop()

    def peek(self):
        if self._is_empty():
            raise Exception("Stack is empty!")
        return self._data[-1]

    def _is_empty(self):
        return len(self._data) == 0


stack = Stack()
stack.push(1)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())




