class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()    # Call the parent class (list class) method
        else:
            raise IndexError("Stack is Empty.")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty.")
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):  # override the insert method in stack (restrict insert method)
        raise AttributeError("No attribute 'insert' in stack.")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Top Element: ", s.peek())
print("Removed Element: ", s.pop())

s.insert(2,40)