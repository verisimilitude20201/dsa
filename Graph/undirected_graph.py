"""
Approach
--------
Representation of an undirected graph using adjacency list.

Complexity:
Space: O(V + E)
Time: O(1) to create a single node/edge
"""
class UndirectedGraph:
    def __init__(self):
        self._adjacency_list = {}
        self._vertex_count = 0
        self._edge_count = 0

    def add_vertex(self, vertex):
        if vertex in self._adjacency_list:
            raise Exception("Vertex already exists")
        self._adjacency_list[vertex] = []
        self._vertex_count += 1

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self._adjacency_list or vertex2 not in self._adjacency_list:
            raise Exception("Vertex not found in Graph")
        self._adjacency_list[vertex1].append(vertex2)
        self._adjacency_list[vertex2].append(vertex1)
        self._edge_count += 1

    def show_connections(self):
        for vertex, edges in self._adjacency_list.items():
            print(vertex + " " + str(edges))


myGraph = UndirectedGraph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')
myGraph.show_connections()
