class Deque:
    def __init__(self, initial_capacity=5):
        self._front = -1
        self._rear = -1
        self._data = [None] * initial_capacity
        self._size = 0

    def enqueue_front(self, element):
        if self.is_empty():
            self._front = self._rear = 0
            self._set_element_at_position(self._front, element)
        elif self.is_full():
            raise Exception("Queue is full")
        elif self._does_front_point_at_first_element():
            self._front = len(self._data) - 1
            self._set_element_at_position(self._front, element)
        else:
            self._front -= 1
            self._set_element_at_position(self._front, element)

        self._increment_size()

    def enqueue_rear(self, element):
        if self.is_empty():
            self._front = self._rear = 0
            self._set_element_at_position(self._rear, element)
        elif self.is_full():
            raise Exception("Queue is full")
        elif self._does_rear_point_at_last_element():
            self._rear = 0
            self._set_element_at_position(self._rear, element)
        else:
            self._rear += 1
            self._set_element_at_position(self._rear, element)

        self._increment_size()

    def _set_element_at_position(self, position, element):
        self._data[position] = element

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)

    def print_queue(self):

        if self.is_empty():
            raise Exception("Queue is empty")

        print(self._data)

    def dequeue_front(self):
        data = None
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self._is_single_element_left():
            data = self._delete_element_at_position(self._front)
            self._make_front_and_rear_point_to_same_element()
            self._decrement_size()
        elif self._does_front_point_to_last_element():
            data = self._delete_element_at_position(self._front)
            self._front = 0
            self._decrement_size()
        else:
            data = self._delete_element_at_position(self._front)
            self._front += 1
            self._decrement_size()

        return data

    def dequeue_rear(self):
        data = None
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self._is_single_element_left():
            data = self._delete_element_at_position(self._rear)
            self._make_front_and_rear_point_to_same_element()
            self._decrement_size()
        elif self._does_rear_point_to_first_element():
            data = self._delete_element_at_position(self._rear)
            self._rear = len(self._data) - 1
            self._decrement_size()
        else:
            data = self._delete_element_at_position(self._rear)
            self._rear -= 1
            self._decrement_size()

        return data

    def _is_single_element_left(self):
        return self._front == self._rear

    def _make_front_and_rear_point_to_same_element(self):
        self._front = self._rear = -1

    def _delete_element_at_position(self, position):
        data = self._data[position]
        self._data[position] = None

        return data

    def _increment_size(self):
        self._size += 1

    def _decrement_size(self):
        self._size -= 1

    def _does_front_point_to_last_element(self):
        return self._front == len(self._data) - 1

    def _does_rear_point_to_first_element(self):
        return self._rear == 0

    def _does_rear_point_at_last_element(self):
        return self._rear == len(self._data) - 1

    def _does_front_point_at_first_element(self):
        return self._front == 0


deque = Deque()
deque.enqueue_front(2)
deque.print_queue()
deque.enqueue_front(4)
deque.print_queue()
deque.enqueue_rear(6)
deque.print_queue()
deque.enqueue_rear(8)
deque.print_queue()
deque.enqueue_front(10)
deque.print_queue()
print(deque.dequeue_front())
deque.print_queue()
print(deque.dequeue_front())
deque.print_queue()
print(deque.dequeue_rear())
deque.print_queue()
print(deque.dequeue_rear())
deque.print_queue()
print(deque.dequeue_rear())
