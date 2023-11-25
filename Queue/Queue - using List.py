from typing import Any

class Queue:
    def __init__(self, front=None, rear=None) -> None:
        self.items = []
        self.front = front
        self.rear = rear
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def enqueue(self, data) -> None:
        self.items.append(data)
        if len(self.items) == 1:
            self.rear = self.front = data
        else:
            self.rear = data
    
    def dequeue(self) -> Any:
        if not self.is_empty():
            data = self.front
            self.items.remove(self.front)
            if len(self.items) > 0:
                self.front = self.items[0]
            else:
                self.front = self.rear = None
            return data
        else:
            raise IndexError("Queue is Empty.")
    
    def get_front(self) -> Any:
        return self.front
    
    def get_rear(self) -> Any:
        return self.rear
    
    def size(self) -> int:
        return len(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(f"Removed Element: {q.dequeue()}")
print(f"Front Element: {q.get_front()}")
print(f"Rear Element: {q.get_rear()}")
print(f"Queue Size: {q.size()}")
