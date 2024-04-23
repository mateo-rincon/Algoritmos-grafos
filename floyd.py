def floyd_warshall(adj_matrix):
    num_vertices = len(adj_matrix)

    # Initialize the distance matrix with the same values as the adjacency matrix
    dist = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = adj_matrix[i][j]

    # Update the distance matrix by considering all intermediate vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # If vertex k is on the shortest path from i to j, update the distance
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage:
adj_matrix = [
    [0, 5, float('inf'), float('inf')],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 7],
    [2, float('inf'), float('inf'), 0]
]
shortest_paths = floyd_warshall(adj_matrix)
for row in shortest_paths:
    print(row)
