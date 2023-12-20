import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.SinglyLinkedList import *

class Stack(SinglyLinkedList):
    def __init__(self, start=None) -> None:
        super().__init__(start)
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return super().is_empty()
    
    def push(self, data) -> None:
        self.insert_at_start(data)
        self.item_count += 1
    
    def pop(self) -> Any:
        if not self.is_empty():
            data = self.start.item
            self.delete_from_start()
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty.")
    
    def size(self) -> int:
        return self.item_count
    
    def insert_at_last(self, data) -> None:
        raise AttributeError("No attribute 'insert_at_last' in stack.")
    
    def insert_after(self, temp, data):
        raise AttributeError("No attribute 'insert_after' in stack.")
    
    def delete_from_last(self):
        raise AttributeError("No attribute 'delete_from_last' in stack.")
    
    def delete_node(self, data):
        raise AttributeError("No attribute 'delete_node' in stack.")
    
    def print_list(self):
        raise AttributeError("No attribute 'print_list' in stack.")
    
    def search_node(self):
        raise AttributeError("No attribute 'search_node' in stack.")
    
    def __iter__(self):
        raise AttributeError("No attribute '__iter__' in stack.")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(f"\nTop Element: {s.peek()}")
print(f"Removed Element: {s.pop()}")
print(f"Stack Size: {s.size()}")

s.insert_at_last(-10)