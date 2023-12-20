class Graph:
    def __init__(self, vertex_count) -> None:
        self.vertex_count = vertex_count
        self.adj_list = { v : [] for v in range(vertex_count) }
    
    def add_edge(self, u, v, weight=1) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertex")
    
    def remove_edge(self, u, v) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print("Invalid Vertex")
    
    def has_edge(self, u, v) -> bool:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, _ in self.adj_list[u])
        else:
            print("Invalid Vertex")
            return False
    
    def print_adj_list(self) -> None:
        for k, v in self.adj_list.items():
            print(f"V{k}: {v}")

graph = Graph(5)

graph.add_edge(1,2)
graph.add_edge(0,3)
graph.add_edge(1,4)
graph.add_edge(4,0)
graph.add_edge(2,4)
graph.remove_edge(0,4)

graph.print_adj_list()