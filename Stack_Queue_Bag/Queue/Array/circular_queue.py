"""
Approach:
--------
Using front and rear pointers we will treat an array as a circular array and wound back front and rear pointers whenever they get past the end of the array

Main conditions

1. Enqueue
    a. front == rear == -1. Array is empty. Reassign both of them to 0 and insert element at rear.
    b. If 1.a is not true, Increment rear by (rear + 1) % length of array and reassign element at rear
    c. Check if (rear + 1) % length of array is equal to front. If yes, the array is full.

2. Dequeue:
    a. Check if front == rear. If so only one element is left and so get it, and set both front and rear to -1 before returning it.
    b. Access the data in array at front and set it to None. Increment front as (front + 1) % length of array. Return the data at front.
    c. Check if array is empty viz.  front == rear == -1. Raise an exception if so.

Complexity:
----------
Time: O(2N) ~ O(N): We are traversing the array both ways front and rear. Since we ignore the constants, this has a linear time complexity.
Space: O(N): Where N is the size of the queue.

Advantages
----------
Helps to avoid wastage of space in queue.

"""
class CircularQueue:
    def __init__(self, initial_capacity=4):
        self._data = [None] * initial_capacity
        self._front = -1
        self._rear = -1

    def enqueue(self, element):
        if self.is_empty():
            self._front = 0
            self._rear = 0
            self._data[self._rear] = element
        elif self.is_full():
            raise Exception("Queue is full")
        else:
            self._rear = (self._rear + 1) % len(self._data)
            self._data[self._rear] = element

    def dequeue(self):
        if self._front == self._rear:
            data = self._data[self._front]
            self._front = self._rear = -1
            return data
        elif self.is_empty():
            raise Exception("Queue is empty")
        else:
            data = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)

            return data

    def is_empty(self):
        return self._front == -1 and self._rear == -1

    def is_full(self):
        return (self._rear + 1) % len(self._data) == self._front


cq = CircularQueue()
cq.enqueue(1)
cq.print_queue()
cq.enqueue(2)
cq.print_queue()
cq.enqueue(3)
cq.print_queue()
cq.enqueue(4)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
