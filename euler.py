def find_eulerian_cycle(adj_matrix):
    # Function to find a cycle from a given vertex using DFS
    def dfs_cycle(v):
        while adj_list[v]:
            u = adj_list[v].pop()
            dfs_cycle(u)
        cycle.append(v)

    num_vertices = len(adj_matrix)
    adj_list = [[] for _ in range(num_vertices)]
    in_degree = [0] * num_vertices
    out_degree = [0] * num_vertices

    # Construct adjacency list and calculate in and out degrees
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
                out_degree[i] += 1
                in_degree[j] += 1

    # Check if the graph has an Eulerian cycle
    if any(in_degree[i] != out_degree[i] for i in range(num_vertices)):
        print("No Eulerian cycle exists")
        return None

    # Find a cycle starting from vertex 0
    cycle = []
    dfs_cycle(0)

    # Reverse the cycle to get the Eulerian cycle
    return cycle[::-1]

# Example usage:
adj_matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]
]
eulerian_cycle = find_eulerian_cycle(adj_matrix)
if eulerian_cycle:
    print("Eulerian Cycle:", eulerian_cycle)
