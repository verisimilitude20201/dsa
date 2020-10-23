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
    first = None
    N = 0
    last = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, data):
        old_last = self.last
        self.last = self.Node(data)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

        self.N += 1


    def dequeue(self):

        data = self.first.data
        self.first = self.first.next
        self.N -= 1

        return data

    def get_size(self):
        return self.N


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    queue = Queue()
    for loop_ctr in range(0, len(A)):
        queue.enqueue(A[loop_ctr])

    while not queue.is_empty():
        print(queue.dequeue())




