from typing import Any

class Node:
    def __init__(self, item=None, prev=None, next=None) -> None:
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self, front=None, rear=None) -> None:
        self.front = front
        self.rear = rear
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.item_count == 0
    
    def insert_front(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
        self.front = node
        self.item_count += 1
    
    def insert_rear(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.front = node
        else:
            node.prev = self.rear
            self.rear.next = node
        self.rear = node
        self.item_count += 1

    def delete_front(self) -> None:
        if not self.is_empty():
            if self.front == self.rear: # only one element in deque
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def delete_rear(self) -> None:
        if not self.is_empty():
            if self.front == self.rear: # only one element in deque
                self.front = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            self.item_count -= 1
        else:
            raise IndexError("Deque is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Deque is Empty.")
    
    def size(self) -> int:
        return self.item_count

dq = Deque()

try:
    print(f"Front Element: {dq.get_front()}")
except IndexError as ex:
    print(ex.args[0])

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