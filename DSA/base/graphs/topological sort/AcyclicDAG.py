class DAG:
  def __init__(self):
    self.graph = []

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = []

  def add_edge(self, start, end):
    if start in self.graph and end in self.graph:
      if self.is_cyclic_util(start, end, set()):
        print("Adding edge will create a cycle. Operation aborted.")
      else:
        self.graph[start].append(end)
    else:
      print("vertex not found in the graph")
    
