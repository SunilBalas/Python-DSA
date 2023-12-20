import sys
import os
from typing import List

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from Stack.Linked_List_Concept import *
from Graph.Adjacency_List_Implementation import *

def Depth_First_Search(graph, source_node) -> List[any]:
    visited_nodes = [False] * graph.vertex_count
    result_nodes = []

    stack = Stack()
    stack.push(source_node)

    while not stack.is_empty():
        u = stack.peek()
        result_nodes.append(u)
        stack.pop()
        visited_nodes[u] = True

        for v in graph.adj_list[u]:
            if not visited_nodes[v[0]]:
                stack.push(v[0])
                visited_nodes[v[0]] = True
        
    return result_nodes


graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(0,3)
graph.add_edge(4,0)
graph.add_edge(1,4)

result = Depth_First_Search(graph, 0)
print(f"DFS: {result}")