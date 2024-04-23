def dijkstra(adj_matrix, start, end):
    num_vertices = len(adj_matrix)

    # Initialize distances from start vertex to all other vertices
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Initialize list to keep track of visited vertices
    visited = [False] * num_vertices

    # Dijkstra's algorithm
    for _ in range(num_vertices):
        # Find the vertex with the minimum distance
        min_distance = float('inf')
        min_vertex = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        # Mark the selected vertex as visited
        visited[min_vertex] = True

        # Stop if the end vertex is reached
        if min_vertex == end:
            break

        # Update distances to neighboring vertices
        for v in range(num_vertices):
            if (not visited[v]) and (adj_matrix[min_vertex][v] != 0) and (distances[min_vertex] + adj_matrix[min_vertex][v] < distances[v]):
                distances[v] = distances[min_vertex] + adj_matrix[min_vertex][v]

    return distances[end]

# Example usage:
adj_matrix = [
    [0, 10, 0, 5, 0],
    [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 3, 9, 0, 2],
    [7, 0, 6, 0, 0]
]
start_vertex = 0
end_vertex = 4
shortest_distance = dijkstra(adj_matrix, start_vertex, end_vertex)
print(f"Shortest distance from vertex {start_vertex} to vertex {end_vertex}: {shortest_distance}")
