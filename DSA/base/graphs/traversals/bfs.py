from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    
    vertex =  queue.popleft()
    print(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(graph, queue, visited )


def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if not vertex in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend([i for i in graph[vertex] if i not in visited])

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("iterative")

bfs_iterative(graph, 'A')

print("Recursive")
bfs_recursive(graph, deque(['A']), set(['A']))