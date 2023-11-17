class Node:
    def __init__(self, item=None, prev=None, next=None) -> None:
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self, start=None) -> None:
        self.start = start
        
    def is_empty(self) -> bool:
        return self.start == None
    
    def print_list(self) -> None:
        if not self.is_empty():
            temp = self.start
            while temp.next is not self.start:
                print(f"[{temp.item}]", end=" ==> ")
                temp = temp.next
            print(f"[{temp.item}]")
        else:
            print("There are no any node available in the list !")
        
    def insert_at_start(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            node.prev = node.next = node
        else:
            node.next = self.start
            node.prev = self.start.prev
            
            self.start.prev.next = node
            self.start.prev = node
        self.start = node
        
    def insert_at_last(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            node.prev = node.next = self.start =  node
        else:
            node.next = self.start
            node.prev = self.start.prev
            
            self.start.prev.next = node
            self.start.prev = node

my_list = CircularDoublyLinkedList()
my_list.insert_at_start(30)
my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.insert_at_last(40)
my_list.insert_at_last(50)
my_list.print_list()