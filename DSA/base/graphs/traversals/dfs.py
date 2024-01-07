def dfs_recursive(graph, start, visited=set()):
    if start not in visited:
        print(start)
        visited.add(start)
        for neighbour in graph[start]:
            dfs_recursive(graph, neighbour, visited)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(
                [neighbor for neighbor in graph[vertex] if neighbor not in visited]
            )


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

print("Recursive")


dfs_recursive(graph, "A")

print("Iterative")

dfs_iterative(graph, "A")
