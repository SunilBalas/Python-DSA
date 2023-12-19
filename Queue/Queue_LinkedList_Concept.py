from typing import Any

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self, front=None, rear=None) -> None:
        self.front = front
        self.rear = rear
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.item_count == 0
    
    def enqueue(self, data) -> None:
        node = Node(data)
        
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        
        self.rear = node
        self.item_count += 1
    
    def dequeue(self) -> None:
        if not self.is_empty():
            if self.front == self.rear: # Only one element in queue
                self.front = self.rear = None
            else:
                self.front = self.front.next
            self.item_count -= 1
        else:
            raise IndexError("Queue is Empty.")
    
    def get_front(self) -> None:
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is Empty.")
    
    def size(self) -> Any:
        return self.item_count

q = Queue()

try:
    q.get_front()
except IndexError as ex:
    print(ex.args[0])

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

try:
    q.dequeue()
except IndexError as ex:
    print(ex.args[0])
    
print(f"Front Element: {q.get_front()}")
print(f"Rear Element: {q.get_rear()}")
print(f"Queue Size: {q.size()}")

