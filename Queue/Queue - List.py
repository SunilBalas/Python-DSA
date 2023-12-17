from typing import Any

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def enqueue(self, data) -> None:
        self.items.append(data)
    
    def dequeue(self) -> None:
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self.items[0] 
        else:
            raise IndexError("Queue is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self.items[-1] 
        else:
            raise IndexError("Queue is Empty.")
    
    def size(self) -> int:
        return len(self.items)

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
