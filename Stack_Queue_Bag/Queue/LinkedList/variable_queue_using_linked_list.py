"""
Concept
--------

Enqueue
-------
1.   None
	 first
	 last

2. 1 -> None
	first
	last

3. 1    		->   2	->	None
  first		   		last
  old_last

4. 1    		->   2	->		3 -> None
  first		   					last
  				  old_last


5. 1  		->   2	->		3 -> 	4	->	None
  first		   						last
  				 		   old_last


6. 1  	->   2	->		3 -> 	4	->	5	-> None
  first		   							last
  				 		   	 old_last

Dequeue
-------
1.  1    2	->	3	->	4	->	5	->	None
 	   first                   last


2.  2   3	->	4	->	5	->	None
 	   first           last


3.  3  	4	->	5	->	None
 	   first   last

4. 4   5 -> None
       first
       last

5. 5  None
	  first
	  last
      
Complexity
----------
O(1) Space/Time
"""
class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._n = 0
    
    def __len(self):
        return self._n

    def enqueue(self, data):
        new_node = self.Node(data)
        if self._tail is None:
            self._tail = new_node
            self._head = self._tail
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        first_node = self._head

        self._head = self._head.next
        self._n -= 1

        return first_node.data

    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self._head.data

    def is_empty(self):
        return self._head is None

if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue("Matt")
    myQueue.enqueue("Powel")
    myQueue.enqueue("Tim")
    myQueue.enqueue("Jim")
    print(myQueue.peek())
    while not myQueue.is_empty():
        print(myQueue.dequeue())




