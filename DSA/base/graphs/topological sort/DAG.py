from collections import defaultdict
class Graph:
  def __init__(self):
    self.graph = defaultdict
  
  def add_edge(self, u, v):
    self.graph[u].append(v)

def topological_sort(graph):
  result = []
  visited = set()
  visited_in_current_dfs = set()
  
  def dfs(vertex):
    if vertex in visited_in_current_dfs:
      raise ValueError("Graph is cyclic")
    visited_in_current_dfs.add(vertex)
    
    for neighbor in graph[vertex]:
      if neighbor not in visited:
        dfs(neighbor)
    visited_in_current_dfs.remove(vertex)
    visited.add(vertex)
    result.insert(0, vertex)
  
  for vertex in graph:
    if vertex not in visited:
      dfs(vertex)
  return result
