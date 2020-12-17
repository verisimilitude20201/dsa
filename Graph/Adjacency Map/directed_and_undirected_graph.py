class Graph:
    class Vertex:

        def __init__(self, element):
            self._element = element

        def __hash__(self):
            return hash(id(self))

        def element(self):
            return self._element

    class Edge:
        def __init__(self, origin, destination, element):
            self._origin = origin
            self._destination = destination
            self._element = element

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            return self._origin if v is self._destination else self._destination

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def insert_vertex(self, element):
        vertex = self.Vertex(element)
        self._outgoing[vertex] = {}
        if self.is_directed():
            self._incoming[vertex] = {}

    def insert_edge(self, origin, destination, element):
        edge = self.Edge(origin, destination, element)
        self._outgoing[origin][destination] = edge
        self._incoming[destination][origin] = edge

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vertex_count(self):
        return len(self._outgoing)

    def get_vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        edge_count = 0
        for vertex in self.get_vertices():
            edge_count += len(self._outgoing[vertex])

        return edge_count if self.is_directed else edge_count // 2

    def edges(self):
        for vertex in self.get_vertices():
            for edge in self._outgoing[vertex]:
                yield edge

    def get_edge(self, origin, destination):
        return self._outgoing[origin][destination]

    def incident_edges(self, v):
        adj = self._incoming if self.is_directed() else self._outgoing
        for edge in self._adj[v]:
            yield edge

    def out_degree(self, v):
        adj = self._outgoing
        return len(adj[v])

    def in_degree(self, v):
        if not self.is_directed():
            return self.out_degree(v)

        adj = self._incoming
        return len(adj[v])