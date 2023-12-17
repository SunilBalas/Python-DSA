class Graph:
    def __init__(self, vertex_count) -> None:
        self.vertex_count = vertex_count
        self.adj_list = { v : [0]*vertex_count for v in range(vertex_count) }
    
    def add_edge(self, u, v, weight=1) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u][v] = self.adj_list[v][u] = weight
        else:
            print("Invalid Vertex")
    
    def remove_edge(self, u, v) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u][v] = self.adj_list[v][u] = 0
        else:
            print("Invalid Vertex")
    
    def has_edge(self, u, v) -> bool:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_list[u][v] != 0
        else:
            print("Invalid Vertex")
    
    def print_adj_list(self) -> None:
        for row_values in self.adj_list.values():
            print(" | ".join(map(str, list(row_values))))

graph = Graph(5)

graph.add_edge(1,2)
graph.add_edge(0,3)
graph.add_edge(1,4)
graph.add_edge(4,0)
graph.add_edge(2,4)
graph.remove_edge(0,4)

graph.print_adj_list()