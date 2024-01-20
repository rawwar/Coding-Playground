import heapq

def prim(graph):
    mst = []
    visited = set()
    start_vertex = 0
    priority_queue = [(0, start_vertex)]
    while priority_queue:
        weight, vertex = heapq.heappop(priority_queue)
        if vertex not in visited:
            visited.add(vertex)
            mst.append((weight, vertex))
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor))
    return mst
