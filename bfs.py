from collections import deque

def bfs(adj_matrix, start):
    cont=0
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    queue = deque()

    # Mark the start vertex as visited and enqueue it
    visited[start] = True
    queue.append(start)

    while queue:
        # Dequeue a vertex from the queue
        current_vertex = queue.popleft()
        print(current_vertex, end=' ')
        cont+=1
        # Visit all adjacent vertices of the current vertex
        for i in range(num_vertices):
            if adj_matrix[current_vertex][i] == 1 and not visited[i]:
                # Mark the adjacent vertex as visited and enqueue it
                visited[i] = True
                queue.append(i)
    return cont


def main(adj_matrix):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices  # Initialize visited array

    # Start BFS from each vertex not yet visited
    for i in range(num_vertices):
        if not visited[i]:
            print("bfs for:"+str(i))
            print("bfs length:"+str(bfs(adj_matrix, i)))

# Example usage:
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
print("BFS Traversal:")
main(adj_matrix)

