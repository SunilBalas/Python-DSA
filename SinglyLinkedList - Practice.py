# Define a node class
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next
        
# Define singly linked list class
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self) -> bool:
        return self.head == None
    
    def print_list(self) -> None:
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                is_last_node = " ==> " if temp.next is not None else ""
                print(f"[{temp.item}]", end=is_last_node)
                temp = temp.next
        else:
            print("There are no any node available in the list !")
            
    def search_node(self, data) -> Node:
        temp = self.head
        
        while temp.next is not None:
            if temp.item == data:
                return temp
            temp = temp.next
            
    def insert_at_first(self, data) -> None:
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_last(self, data) -> None:
        node = Node(data)
        
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.head = node
        
    def insert_after_node(self, node, data) -> None:
        if not self.is_empty():
            new_node = Node(data, node.next)
            node.next = new_node
            
    def delete_from_first(self) -> None:
        if not self.is_empty():
            self.head = self.head.next
            
    def delete_from_last(self) -> None:
        if self.head is None: # Empty list
            return None
        elif self.head.next is None: # At least one node
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            
    def delete_from_node(self, data) -> None:
        if self.head is None: # Empty list
            return None
        elif self.head.next is None and self.head.item == data: # At least one node
            self.head = None
        else:
            temp = self.head
            
            if temp.item == data:
                self.head = None
                
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                
    def __iter__(self):
        return SLLIterator(self.head)

class SLLIterator:
    def __init__(self, start) -> None:
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.item
        self.current = self.current.next
        
        return data

lst = SinglyLinkedList()
lst.insert_at_first(30)
lst.insert_at_first(20)
lst.insert_at_first(10)
lst.insert_at_last(50)
lst.insert_after_node(lst.search_node(30), 40)
lst.print_list()
lst.delete_from_first()
lst.delete_from_last()
lst.delete_from_node(30)
print()
lst.print_list()
print()

# Using Iterator
for i in lst:
    print(f"[{i}]", end=" ")