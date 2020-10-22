"""
ADT for a Stack of fixed size Using an array

Space/Time complexity: O(1) each
"""
class FixedStackOfElements:
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.stack_list = [None] * self.size

    def push(self, data):
        if self.top == self.size:
            raise Exception("Stack is Full")
        self.stack_list[self.top] = data
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise Exception("Stack is empty")
        self.top -= 1
        popped_element = self.stack_list[self.top]

        return popped_element

    def peek(self):
        if self.top == 0:
            raise Exception("Stack is empty")
        return self.stack_list[self.top]


if __name__ == '__main__':
    stack_of_numbers = FixedStackOfElements(8)
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    for number in range(len(A)):
        stack_of_numbers.push(A[number])

    while True:
        element = stack_of_numbers.pop()
        if element is None:
            break
        print(element)

