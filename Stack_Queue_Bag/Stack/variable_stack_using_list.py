"""
Concept
----------

We push and pop both at the first element of the list, thereby avoiding the need to iterate over

1. Push stores the older first, creates a new node. It assigns the next of the new node to the older first. It sets the new node to first.

Push
------
1. 	None
	first

2. 1 			-> None
   first

3. 2 		-> 1 		-> None	
   first    old_first


3. 3	->		2 		->   1 		-> None	
   first    old_first


4. 4	->		3	->		2 		->   1 		-> None	
   first    old_first

5. 5 -> 		4		->		3	->		2 		->   1 		-> None	
   first    old_first


2. Pop just returns the data of the first pointer of linked list and increments it to point to next node.

Pop
---

1. 5 -> 		4		->		3	->		2 		->   1 		-> None	
   first.data   


2. 	4		  ->	3	->		2 		->   1 		-> None	
   first.data 


3. 	3	->		2 		->   1 		-> None	
   first.data


4. 2 		->   1 		-> None	
   first.data  

5. 1 		-> None	
   first.data

6. first 
   None


Complexity
----------
O(1) Space/Time

"""
class Stack1:
    N = 0
    first = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, data):
        node = self.Node(data)
        if self.first is not None:
            old_first = self.first
            node.next = old_first
        self.first = node
        self.N += 1

    def pop(self):
        data = self.first.data
        self.first = self.first.next
        self.N -= 1

        return data

    def is_empty(self):
        return self.first == None

    def peek(self):
        return self.first.data


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    stack = Stack()
    for loop_ctr in range(0, len(A)):
        stack.push(A[loop_ctr])

    while not stack.is_empty():
        print(stack.pop())


class Stack2:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        first_node = self.head
        self.head = self.head.next
        return first_node.data

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.head.data

    def is_empty(self):
        return self.head is None


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
