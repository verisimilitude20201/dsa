
class SingleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    def append(self, data, node=None):
        temp_node = SingleLinkedList.Node(data)
        if node is None:
            node = temp_node
        else:
            temp_node2 = node
            while temp_node2.next is not None:
                temp_node2 = temp_node2.next
            temp_node2.next = temp_node
        return node

    def traverse(self, node):
        node_list = ""
        while node:
            node_list += str(node.data) + "-->"
            if node.next is None:
                node_list += "NULL"
            node = node.next

        return node_list


if __name__=='__main__':
    A = [1, 2, 3, 4, 5]
    slist = SingleLinkedList()
    node = None
    for loop_ctr in range(0, len(A)):
        node = slist.append(A[loop_ctr], node)
    slist.traverse(node)