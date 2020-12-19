"""
Returns a transitive closure of a graph

Complexity
---------
Space: O(m + n)
Time: O(n^3)

DISCLAIMER - YET TO TEST
"""

def flow_warshall(G):
	g1 = deepcopy(g)
	vertices_of_g = vertices(g)
	n = len(vertices_of_g)
	for k in range(n):
		for i in range(n):
			if i != k and g1.get_edge(i, k) is not None:
				for j in range(n):
					if i != j != k and g1.get_edge(k, j) is not None:
						if g1.get_edge(i, j) is None:
							g1.insert_edge(vertices_of_g[i], vertices_of_g[j])
    
    return g1