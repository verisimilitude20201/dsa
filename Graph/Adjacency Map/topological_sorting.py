"""
Returns a topological order of a Graph

Complexity
---------
Space: O(n)
Time: O(m + n)

DISCLAIMER - YET TO TEST
"""

def topological_sorting(G):
    topo = []
    ready = []
    incount = {}
    for u in g.vertices():
        incount[u] = g.in_degree(u, False)
        if incount[u] == 0:
            ready.append(u)

    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(u)

    return topo