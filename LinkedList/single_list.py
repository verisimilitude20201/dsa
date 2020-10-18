class SingleLinkedList:
    nodes = None

    size = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def insert_data_after_index(self, data, index):
        """
        O(N): Time, O(1) Space
        1. Time complexity is O(N) worst-case
        2. Space complexity is O(1) because we're allocating just one memory location for the node.
        :param data:
        :param index:
        :return:
        """

        if index <= 0:
            self.prepend_and_increment_size(data)
        elif index >= self.size:
            self.append_and_increment_size(self, data)
        else:
            index_counter = 0
            node = SingleLinkedList.Node(data)
            temp_node = self.nodes
            while index_counter < index:
                temp_node = temp_node.next
                index_counter += 1
            current_next = temp_node.next
            temp_node.next = node
            node.next = current_next
        self.increment_size()


    def prepend_and_increment_size(self, data):
        """
        O(1) Time/Space.
            1. Time: We are prepending an element to the front of the linkedlist so O(1).
            2. Space: We are just allocating space for 1 node so O(1)
        :param data:
        :return:
        """
        node = SingleLinkedList.Node(data)
        if self.nodes is None:
            self.nodes = node
        else:
            current_first_node = self.nodes
            node.next = current_first_node
            self.nodes = node
        self.increment_size()

    def append_and_increment_size(self, data):
        """
        O(N) Time, O(1) Space
        1. Time: We are iterating through N-1 nodes to get to the Nth node to append data after that node.
        2. Space: We are just constructing one node. However, if we are creating a list within for-loop, this will also be O(N)
        :param data:
        :return:
        """
        node = SingleLinkedList.Node(data)
        if self.nodes is None:
            self.nodes = node
        else:
            temp_node = self.nodes
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = node

        self.increment_size()

    def increment_size(self):
        self.size += 1

    def decrement_size(self):
        self.size -= 1

    def traverse(self):
        """
        O(N) Time, O(1) Space
        1. Time: We iterate through N elements hence O(N)
        2. Space: We are'nt allocating any new memory.
        :return:
        """
        node_list = ""
        while self.nodes:
            node_list += str(self.nodes.data) + "-->"
            if self.nodes.next is None:
                node_list += "NULL"
            self.nodes = self.nodes.next

        return node_list

    def delete_data_and_decrement_size(self, data):
        """
        1. Time Complexity: O(N)
          --> We do N lookups to find the data to delete
        2. Space Complexity: O(1)
          --> We deallocate just one node.

        :param data:
        :return:
        """
        if self.nodes.data == data:
            self.nodes = self.nodes.next
            self.decrement_size()
            return True
        temp_node = self.nodes
        prev_node = None
        while temp_node:
            if temp_node.data == data:
                break
            prev_node = temp_node
            temp_node = temp_node.next
        if temp_node is not None:
            prev_node.next = temp_node.next
            temp_node = None
            self.decrement_size()
            return True

        return False


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    slist = SingleLinkedList()
    for loop_ctr in range(0, len(A)):
        slist.append_and_increment_size(A[loop_ctr])
    slist.prepend_and_increment_size(3)
    print(slist.delete_data_and_decrement_size(3))
    print(slist.insert_data_after_index(3.5, 2))
    print(slist.traverse())
    print(slist.size)
