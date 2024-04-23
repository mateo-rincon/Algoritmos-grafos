def is_valid(v, graph, path, pos):
    # Check if vertex v can be added to the Hamiltonian cycle
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if vertex v is already in the path
    for vertex in path:
        if vertex == v:
            return False

    return True

def hamiltonian_util(graph, path, pos):
    # Base case: If all vertices are included in the path
    if pos == len(graph):
        # Check if there is an edge from the last vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as the next candidate in Hamiltonian cycle
    for v in range(1, len(graph)):
        if is_valid(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            # Backtrack if adding vertex v does not lead to a solution
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    num_vertices = len(graph)
    path = [-1] * num_vertices
    path[0] = 0  # Start from vertex 0

    if not hamiltonian_util(graph, path, 1):
        print("No Hamiltonian cycle exists")
        return False

    print("Hamiltonian Cycle:")
    print(*path, path[0])
    return True

# Example usage:
adj_matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]
]
print(hamiltonian_cycle(adj_matrix))
