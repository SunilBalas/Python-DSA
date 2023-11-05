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

myList = DoublyLinkedList()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.print_list()