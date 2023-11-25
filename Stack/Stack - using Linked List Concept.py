from typing import Any

class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Stack:
    def __init__(self, top=None) -> None:
        self.top = top
        self.item_count = 0
    
    def is_empty(self) -> bool:
        return self.top == None
    
    def push(self, data) -> None:
        node = Node(data, self.top)
        self.top = node
        self.item_count += 1
    
    def pop(self) -> Any:
        if not self.is_empty():
            data = self.top.item
            self.top = self.top.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError("Stack is Empty.")
    
    def size(self) -> int:
        return self.item_count

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(f"Top Element: {s.peek()}")
print(f"Removed Element: {s.pop()}")
print(f"Stack Size: {s.size()}")