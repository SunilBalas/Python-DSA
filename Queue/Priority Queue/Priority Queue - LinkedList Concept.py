from typing import Any

class Node:
    def __init__(self, item=None, priority=None, next=None) -> None:
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.item_count == 0
    
    def push(self, data, priority) -> None:
        node = Node(data, priority)
        if not self.start or priority < self.start.priority:
            node.next = self.start
            self.start = node
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            node.next = temp.next
            temp.next = node
        self.item_count += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Priority Queue is Empty.")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data
    
    def size(self) -> int:
        return self.item_count

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