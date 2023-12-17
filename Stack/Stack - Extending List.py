from typing import Any

class Stack(list):
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def push(self, data) -> None:
        self.append(data)
    
    def pop(self) -> Any:
        if not self.is_empty():
            '''
                - Call the parent class (list class) method 
                    otherwise it will call itself and will go into infinite call
            '''
            return super().pop()
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty.")
    
    def size(self) -> int:
        return len(self)
    
    def insert(self, index, data) -> None:  # override the insert method in stack (restrict insert method)
        raise AttributeError("No attribute 'insert' in stack.")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("Top Element: ", s.peek())
print("Removed Element: ", s.pop())

s.insert(2,40)