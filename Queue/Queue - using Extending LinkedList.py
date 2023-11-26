import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.SinglyLinkedList import *

class Queue(SinglyLinkedList):
    def __init__(self, start=None) -> None:
        super().__init__(start)
        self.rear = None
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return super().is_empty() # Call the parent class (SinglyLinkedList) method
    
    def enqueue(self, data) -> None:
        self.insert_at_last(data)
        self.rear = data
        self.item_count += 1
    
    def dequeue(self) -> None:
        if not self.is_empty():
            self.delete_from_start()
            if self.start is None:
                self.rear = None
            self.item_count -= 1
        else:
            raise IndexError("Queue is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Queue is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Queue is Empty.")
    
    def size(self) -> int:
        return self.item_count
    
    def insert_at_start(self, data) -> None:
        raise AttributeError("No attribute 'insert_at_start' in queue.")
    
    def insert_after(self, temp, data):
        raise AttributeError("No attribute 'insert_after' in queue.")
    
    def delete_from_last(self):
        raise AttributeError("No attribute 'delete_from_last' in queue.")
    
    def delete_node(self, data):
        raise AttributeError("No attribute 'delete_node' in queue.")
    
    def print_list(self):
        raise AttributeError("No attribute 'print_list' in queue.")
    
    def search_node(self):
        raise AttributeError("No attribute 'search_node' in queue.")
    
    def __iter__(self):
        raise AttributeError("No attribute '__iter__' in queue.")

q = Queue()

try:
    q.get_front()
except IndexError as ex:
    print(f"\n{ex.args[0]}")

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

try:
    q.dequeue()
except IndexError as ex:
    print(ex.args[0])

try:
    print(f"Front Element: {q.get_front()}")
except IndexError as ex:
    print(f"\n{ex.args[0]}")

try:
    print(f"Rear Element: {q.get_rear()}")
except IndexError as ex:
    print(f"\n{ex.args[0]}")

print(f"Queue Size: {q.size()}")

try:
    q.delete_from_last()
except AttributeError as ex:
    print(f"\n{ex.args[0]}")