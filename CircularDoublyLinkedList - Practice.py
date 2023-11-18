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
            
    def search_node(self, data) -> Node:
        if self.is_empty():
            return None
        else:
            temp = self.start
            while temp.next is not self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
            return None

    def insert_after_node(self, temp, data) -> None:
        if temp is not None:
            node = Node(data, temp, temp.next)
            temp.next.prev = node
            temp.next = node
            
    def delete_from_start(self) -> None:
        if not self.is_empty():
            if self.start.next is self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
                
    def delete_from_last(self) -> None:
        if not self.is_empty():
            if self.start.next is self.start:
                self.start = None
            else:
                self.start.prev = self.start.prev.prev
                self.start.prev.next = self.start

    def delete_node(self, data) -> None:
        if self.is_empty():
            return None
        elif self.start.next is self.start:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.delete_from_start()
            while temp.next is not self.start:
                if temp is self.start.prev:
                    if temp.item == data:
                        self.delete_from_last()
                        break
                if temp.item == data:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                    break
                temp = temp.next
            if temp is self.start.prev:
                if temp.item == data:
                    self.delete_from_last()
                    
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self, start) -> None:
        self.current = start
        self.start = start
        self.flag = False   # check for the flag that list is again points to first node
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current is self.start and self.flag:
            raise StopIteration
        else:
            self.flag = True
        
        data = self.current.item
        self.current = self.current.next
        
        return data

my_list = CircularDoublyLinkedList()
my_list.insert_at_start(30)
my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.print_list()
my_list.insert_at_last(40)
my_list.insert_at_last(60)
my_list.print_list()
my_list.insert_after_node(my_list.search_node(40), 50)
my_list.print_list()
my_list.delete_from_start()
my_list.print_list()
my_list.delete_from_last()
my_list.print_list()
my_list.delete_node(20)
my_list.delete_node(30)
my_list.print_list()

for i in my_list:
    print(f"[{i}]", end=" ==> ")