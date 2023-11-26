import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.DoublyLinkedList import *

class Deque:
    def __init__(self) -> None:
        self.dll = DoublyLinkedList()
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.item_count == 0
    
    def insert_front(self, data) -> None:
        self.dll.insert_at_start(data)
        self.item_count += 1
    
    def insert_rear(self, data) -> None:
        self.dll.insert_at_last(data)
        self.item_count += 1
    
    def delete_front(self) -> None:
        if not self.is_empty():
            self.dll.delete_from_start()
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def delete_rear(self) -> None:
        if not self.is_empty():
            self.dll.delete_from_last()
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.dll.start.item
        else:
            raise IndexError("Deque is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            temp = self.dll.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Deque is Empty.")
    
    def size(self) -> int:
        return self.item_count

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