import sys
import os
from typing import Any

# Stores the current working directory to system path
sys.path.append(os.path.abspath(os.getcwd()))

from LinkedList.SinglyLinkedList import *

class Queue:
    def __init__(self) -> None:
        self.sll = SinglyLinkedList()
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.sll.is_empty()
    
    def enqueue(self, data) -> None:
        self.sll.insert_at_last(data)
        self.item_count += 1
    
    def dequeue(self) -> None:
        if not self.is_empty():
            self.sll.delete_from_start()
            self.item_count -= 1
        else:
            raise IndexError("Queue is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.sll.start.item
        else:
            raise IndexError("Queue is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            temp = self.sll.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Queue is Empty.")
    
    def size(self) -> int:
        return self.item_count

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
