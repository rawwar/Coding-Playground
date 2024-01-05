from collections import defaultdict

class UndirectedGraphUsingMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0]*num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, start, end):
        self.matrix[start][end] = 1
        self.matrix[end][start] = 1
    
    def display(self):
        for row in self.matrix:
            print(row)


class UndirectedGraphUsingAdjacencyList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")




if __name__ == "__main__":
    print("Undirected graph: using matrix")
    graph_matrix = UndirectedGraphUsingMatrix(5)
    graph_matrix.add_edge(0, 1)
    graph_matrix.add_edge(0, 4)
    graph_matrix.add_edge(1, 2)
    graph_matrix.add_edge(1, 3)
    graph_matrix.add_edge(1, 4)
    graph_matrix.add_edge(2, 3)
    graph_matrix.add_edge(3, 4)

    graph_matrix.display()

    print("-"*10)

    print("Undirected graph using Adjancy list")
    obj2 = UndirectedGraphUsingAdjacencyList()
    obj2.add_edge(0, 1)
    obj2.add_edge(0, 4)
    obj2.add_edge(1, 2)
    obj2.add_edge(1, 3)
    obj2.add_edge(1, 4)
    obj2.add_edge(2, 3)
    obj2.add_edge(3, 4)

    obj2.display()
    print("-"*10)