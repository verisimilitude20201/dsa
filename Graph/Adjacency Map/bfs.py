"""
Breadth-First Search using a List

Complexity
-----------
Space: O(n) Uses an auxillary dictionary to hold n vertices
Time: (m + n) Here n is the number of levels and m is the number of adjacent vertexes from a given vertex
"""

from directed_and_undirected_graph import Graph

def bfs(G, s):
    discovered = {s: None}
    level = [s]
    while len(level) > 0:
        next_level = []
        for vertex in level:
            for edge in G.incident_edges(vertex):
                opposite_endpoint = edge.opposite(vertex)
                if opposite_endpoint not in discovered:
                    discovered[opposite_endpoint] = edge
                    next_level.append(opposite_endpoint)
        level = next_level

        return discovered


G = Graph()
vertexU = G.insert_vertex('u')
vertexV = G.insert_vertex('v')
vertexW = G.insert_vertex('w')
vertexZ = G.insert_vertex('z')
G.insert_edge(vertexU, vertexV, 'e')
G.insert_edge(vertexV, vertexW, 'f')
G.insert_edge(vertexU, vertexW, 'g')
G.insert_edge(vertexW, vertexZ, 'h')


print(bfs(G, vertexU))