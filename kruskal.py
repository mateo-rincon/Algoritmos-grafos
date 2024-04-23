class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # They are already in the same set

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True

def kruskal(adj_matrix):
    num_vertices = len(adj_matrix)
    edges = []

    # Convert adjacency matrix to list of edges
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adj_matrix[i][j] != 0:  # Assuming 0 indicates absence of an edge
                edges.append((i, j, adj_matrix[i][j]))

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Initialize disjoint set
    ds = DisjointSet(num_vertices)

    # Initialize minimum spanning tree
    mst = []

    # Iterate over sorted edges
    for edge in edges:
        u, v, weight = edge
        if ds.union(u, v):
            mst.append(edge)

    return mst

# Example usage:
adj_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst = kruskal(adj_matrix)
print("Minimum Spanning Tree (Edges):")
for edge in mst:
    print(edge)
