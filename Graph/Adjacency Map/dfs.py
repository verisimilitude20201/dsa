"""
1. DFS Algorithm using Recursion and HashTable
2. Application of DFS algorithm to check if path exists from u to v

Complexity
----------

A. DFS

1. Space Complexity: O(n) where n is the number vertices
2. Time complexity: O(ns + ms) where ns is the number of vertices reachable from s and ms is the number of edges incident to those vertices.

B. If Path exists from u to v

1. Space complexity: O(n) n being the number of nodes on the path
2. Time complexity: O(n) n being the number of nodes on the path

"""

from directed_and_undirected_graph import Graph


def dfs(G, u, discovered):
    for edge in G.incident_edges(u):
        v = edge.opposite(u)
        if v not in discovered:
            discovered[v] = edge
            dfs(G, v, discovered)

def connected_path(u, v, discovered):
    start = v
    path = [v]
    while start is not u:
        incident_edge_to_v = discovered[v]
        parent = incident_edge_to_v.opposite(v)
        path.append(parent)
        start = parent

    path.reverse()

    return path

G = Graph()
vertexU = G.insert_vertex('u')
vertexV = G.insert_vertex('v')
vertexW = G.insert_vertex('w')
vertexZ = G.insert_vertex('z')
G.insert_edge(vertexU, vertexV, 'e')
G.insert_edge(vertexV, vertexW, 'f')
G.insert_edge(vertexU, vertexW, 'g')
G.insert_edge(vertexW, vertexZ, 'h')
for edge in G.incident_edges(vertexU):
    print(edge)

result = {vertexU: None}
dfs(G, vertexU, result)
print(result)




print(connected_path(vertexU, vertexV, result))




