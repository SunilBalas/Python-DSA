from typing import Any

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def push(self, data) -> None:
        self.items.append(data)
    
    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty.")
    
    def size(self) -> int:
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(f"Top Element: {s.peek()}")
print(f"Removed Element: {s.pop()}")
print(f"Stack Size: {s.size()}")