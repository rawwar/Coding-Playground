from collections import defaultdict, deque

def topological_sort(graph):
    indegree = defaultdict(int)
    for vertices in graph.values():
        for vertex in vertices:
            indegree[vertex] += 1
    print(dict(indegree))
    
    queue = deque([v for v in graph if indegree[vertex]==0])
    top_order = []
    
    while queue:
        current = queue.popleft()
        top_order.append(current)
        
        for n in graph[current]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)
    if len(top_order) != len(graph):
        print("Cycles found")
    else:
        print(top_order)


graph = {
    1: [2, 4],
    2: [3],
    3: [],
    4: [3]
}

topological_sort(graph)