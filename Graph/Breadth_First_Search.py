import sys
import os
from typing import List

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from Queue.Queue_LinkedList_Concept import *
from Graph.Adjacency_Matrix_Implementation import *

def Breadth_First_Search(self, graph, source_node) -> List[any]:
    visited_nodes = [False] * graph.vertex_count
    result_nodes = []
    
    queue = Queue()
    queue.enqueue(source_node)
    
    while not queue.is_empty():
        element = queue.get_front()
        result_nodes.append(element)
        queue.dequeue()
        visited_nodes[element] = True
        
        # TODO: To Be Continue....




graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(0,3)
graph.add_edge(4,0)
graph.add_edge(1,4)

Breadth_First_Search(graph, 0)