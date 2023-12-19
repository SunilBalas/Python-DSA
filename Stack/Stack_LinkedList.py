import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.SinglyLinkedList import *

class Stack:
    def __init__(self) -> None:
        self.sll = SinglyLinkedList()
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.sll.is_empty()
    
    def push(self, data) -> None:
        self.sll.insert_at_start(data)
        self.item_count += 1
    
    def pop(self) -> Any:
        if not self.is_empty():
            data = self.sll.start.item
            self.sll.delete_from_start()
            self.item_count -= 1
            return data
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.sll.start.item
    
    def size(self) -> int:
        return self.item_count

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("\nTop Element: ", s.peek())
print("Removed Element: ", s.pop())
print("Stack Size: ", s.size())