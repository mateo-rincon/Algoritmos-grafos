
def dfs(adj_matrix, start):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    length=[0]
    # Helper function for DFS traversal
    def dfs_visit(vertex):
        visited[vertex] = True
        print(vertex, end=' ')
        length[0]+=1
        # Visit all adjacent vertices of the current vertex
        for i in range(num_vertices):
            if adj_matrix[vertex][i] == 1 and not visited[i]:
                dfs_visit(i)

    # Start DFS traversal from the start vertex
    dfs_visit(start)
    return length[0]
# Example usage:
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
start_vertex = 0
print("DFS Traversal:")

print("DFS length:"+str(dfs(adj_matrix, start_vertex)))
