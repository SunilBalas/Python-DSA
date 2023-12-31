import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.DoublyLinkedList import *

class Deque(DoublyLinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.rear = None
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return super().is_empty()
    
    def insert_front(self, data) -> None:
        self.insert_at_start(data)
        
        if self.start.next is None:
            self.rear = data
            
        self.item_count += 1
    
    def insert_rear(self, data) -> None:
        self.insert_at_last(data)
        self.rear = data
        self.item_count += 1
    
    def delete_front(self) -> None:
        if not self.is_empty():
            self.delete_from_start()
            if self.start is None:
                self.rear = None
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def delete_rear(self) -> None:
        if not self.is_empty():
            self.delete_from_last()
            
            if self.start is None:
                self.rear = None
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                self.rear = temp.item
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Deque is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Deque is Empty.")
    
    def size(self) -> int:
        return self.item_count
    
    def insert_after(self, temp, data) -> None:
        raise AttributeError("No attribute 'insert_after' in queue.")
    
    def delete_node(self, data) -> None:
        raise AttributeError("No attribute 'delete_node' in queue.")
    
    def print_list(self) -> None:
        raise AttributeError("No attribute 'print_list' in queue.")
    
    def search_node(self, data) -> None:
        raise AttributeError("No attribute 'search_node' in queue.")
    
    def __iter__(self) -> None:
        raise AttributeError("No attribute '__iter__' in queue.")

dq = Deque()

try:
    print(f"Front Element: {dq.get_front()}")
except IndexError as ex:
    print(f"\n{ex.args[0]}")

dq.insert_front(30)
dq.insert_front(20)
dq.insert_front(10)
dq.insert_rear(40)
dq.insert_rear(50)

try:
    dq.delete_front()
except IndexError as ex:
    print(ex.args[0])

try:
    dq.delete_rear()
except IndexError as ex:
    print(ex.args[0])

print(f"Front Element: {dq.get_front()}")
print(f"Rear Element: {dq.get_rear()}")
print(f"Deque Size: {dq.size()}")

try:
    search_node = None
    try:
        search_node = dq.search_node(20)
    except AttributeError as ex:
        print(ex.args[0])
        
    dq.insert_after(search_node, -10)
except AttributeError as ex:
    print(ex.args[0])