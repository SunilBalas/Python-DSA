class Graph:
    def __init__(self, vertex_count) -> None:
        self.vertex_count = vertex_count
        self.adj_matrix = [[0]*vertex_count for v in range(vertex_count)]
    
    def add_edge(self, u, v, weight=1) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
    
    def remove_edge(self, u, v) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")
    
    def has_edge(self, u, v) -> bool:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex")
    
    def print_adj_matrix(self) -> None:
        for row_list in self.adj_matrix:
            print(" | ".join(map(str, row_list)))

graph = Graph(5)

graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(0,3)
graph.add_edge(4,0)
graph.add_edge(1,4)
graph.remove_edge(2,3)

print(f"{graph.has_edge(4,1)}")
graph.print_adj_matrix()