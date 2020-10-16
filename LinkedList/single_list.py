
class SingleLinkedList:

    nodes = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def prepend(self, data):
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

    def append(self, data):
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
        return node

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

    def delete_data(self, data):
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
            return True
        return False


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    slist = SingleLinkedList()
    for loop_ctr in range(0, len(A)):
        slist.append(A[loop_ctr])
    slist.prepend(3)
    print(slist.delete_data(3))
    print(slist.traverse())
