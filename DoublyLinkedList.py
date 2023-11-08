class Node:
    def __init__(self, item=None, prev=None, next=None) -> None:
        self.item = item
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
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
        return None
        
    def insert_at_start(self, data) -> None:
        '''
            - Create a new node with data, previous reference is None and next reference is head pointer
            - if head pointer is not None then assign the previous reference of head to new node
            - Assign new node reference to head pointer
        '''
        node = Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        
    def insert_at_last(self, data) -> None:
        '''
            - Create a new node with data and previous as well as next reference set to None
                because next reference is None as it is going to be the last node and previous
                reference is currently set to None because we don't know the current last node.
                We need to traverse through the list
            - Traverse from head to current last node, and after that assign the new node reference 
                to next of the current last node and assign the current last node reference to previous 
                of the new node
            - If list is empty then just assign the new node reference to head pointer
        '''
        node = Node(data)
        
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp
        else:
            self.head = node # Empty List
            
    def insert_after_node(self, node, data) -> None:
        '''
            - Create a new node with data, previous reference to given node
                and next reference to next reference of given node
            - Assign the reference of new node to previous of next reference of given node
            - Assign the reference of new node to next reference of given node
        '''
        
        if node is not None:
            new_node = Node(data, node, node.next)
            if node.next is not None:
                node.next.prev = new_node
                node.next = new_node
                
    def delete_from_start(self) -> None:
        '''
            - Assign the reference of second node to head pointer
            - If list is not empty then assign the None to previous reference of
                second node because it is a first node now.
        '''
        
        if not self.is_empty():
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
    
    def delete_from_last(self) -> None:
        if self.head is None:   # Empty list
            return None
        elif self.head.next is None:    # Only one node
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            
    def delete_node(self, data):
        if self.head is None:   # Empty list
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:   # Node is in between the list or node is not at the end
                        temp.next.prev = temp.prev
                        
                    if temp.prev is not None: # Node is in between the list or node is not at the start
                        temp.prev.next = temp.next
                    else:                       # Only one node
                        self.head = temp.next
                    break                    
                temp = temp.next
                
    def __iter__(self):
        return DLLIterator(self.head)

# Doubly Linked List using iterator
class DLLIterator:
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

myList = DoublyLinkedList()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.print_list()
print()
myList.insert_at_last(50)
myList.print_list()
print()
myList.insert_after_node(myList.search_node(30), 40)
myList.print_list()
print()
myList.delete_from_start()
myList.print_list()
print()
myList.delete_from_last()
myList.print_list()
print()
myList.delete_node(20)
myList.print_list()
print()

for i in myList:
    print(f"[{i}]", end=" ==> ")