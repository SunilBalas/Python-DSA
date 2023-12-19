from typing import Any

class Deque(list):
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def insert_front(self, data) -> None:
        self.insert(0, data)
    
    def insert_rear(self, data) -> None:
        self.append(data)
    
    def delete_front(self) -> None:
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("Deque is Empty.")
    
    def delete_rear(self) -> None:
        if not self.is_empty():
            self.pop()
        else:
            raise IndexError("Deque is Empty.")
    
    def get_front(self) -> Any:
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Deque is Empty.")
    
    def get_rear(self) -> Any:
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Deque is Empty.")
    
    def size(self) -> int:
        return len(self)

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