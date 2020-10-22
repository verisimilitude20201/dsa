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
class Stack:
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

