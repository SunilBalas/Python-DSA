import sys
import os
from typing import List

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from Queue.LinkedList_Concept import *
from Graph.Adjacency_Matrix_Implementation import *

def Breadth_First_Search(graph, source_node) -> List[any]:
    visited_nodes = [False] * graph.vertex_count
    result_nodes = []

    queue = Queue()
    queue.enqueue(source_node)

    while not queue.is_empty():
        u = queue.get_front()
        result_nodes.append(u)
        queue.dequeue()
        visited_nodes[u] = True

        for v in range(graph.vertex_count):
            if graph.has_edge(u, v) and not visited_nodes[v]:
                queue.enqueue(v)
                visited_nodes[v] = True
        
    return result_nodes


graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(0,3)
graph.add_edge(4,0)
graph.add_edge(1,4)

result = Breadth_First_Search(graph, 0)
print(f"BFS: {result}")