from typing import Any

class PriorityQueue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def push(self, data, priority) -> None:
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Priority Queue is Empty.")
        return self.items.pop(0)[0]
    
    def size(self) -> int:
        return len(self.items)

pq = PriorityQueue()

pq.push(10, 1)
pq.push(30, 4)
pq.push(20, 2)
pq.push(50, 4)
pq.push(25, 3)
pq.push(40, 5)

print(f"Priority Queue Size: {pq.size()}")

while not pq.is_empty():
    print(f"Removed Element: {pq.pop()}")