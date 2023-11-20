class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next
    
class SinglyLinkedList:
    def __init__(self, start=None) -> None:
        self.start = start
        
    def is_empty(self) -> bool:
        '''
            - If start is points to node means linked list is empty
        '''
        return self.start == None
    
    def insert_at_start(self, data) -> None:
        '''
            - Create a new node which has item equals data and points to the node which start points to
            - If start points to None then new node points to None
            
            - For creating link, give reference of new node to start pointer
        '''
        node = Node(data, self.start)
        self.start = node
        
    def insert_at_last(self, data) -> None:
        '''
            - New node points to None because it is at last
            
            - Create a temp variable to track the node
            - Assign the reference of start to temp
            
            - Traverse the linked list until find the node which points to None and that is the last node
            
            - Assign the next reference of the temp to temp
            
            - Once the temp is at last which means now temp.next points to None
            - Assign the reference of new node to temp
        '''
        node = Node(data)
        
        if not self.is_empty():
            temp = self.start
            
            while temp.next is not None:
                temp = temp.next
            
            temp.next = node
        else:
            self.start = node
            
    def search_node(self, data):
        '''
            - Initially, assign the reference of start to temp variable
            
            - Traverse in linked list until the temp is not None
            - If data of temp is search data then return the temp otherwise move forward
            - If no node matches the search data then return None
        '''
        temp = self.start
        
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
            
    def insert_after(self, temp, data):
        '''
            - Insert the new node after temp node
            - Create the new node with data and it points to the node which currently temp points
            - Assign the reference of new node to temp node
        '''
        if temp is not None:
            node = Node(data, temp.next)
            temp.next = node
            
    def print_list(self):
        temp = self.start
        
        while temp is not None:
            if temp.next is None:
                print(f"[{temp.item}]")
            else:
                print(f"[{temp.item}]", end=" ==> ")
            temp = temp.next
            
            
    def delete_from_start(self):
        if self.start is not None:
            self.start = self.start.next
            
    def delete_from_last(self):
        '''
            - Empty list
            
            - Only one node then delete that node
        '''
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            '''
                - temp.next.next is second last node
            '''
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            
    def delete_node(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    
    def __iter__(self):
        return SLLIterator(self.start)

'''
    Create an iterator for the Singly Linked List
'''
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
    
    
'''
    Create the object of Singly Linked List
'''
myList = SinglyLinkedList()
myList.insert_at_last(10)
myList.insert_at_start(15)
myList.insert_at_last(23)
myList.insert_at_start(43)
myList.insert_after(myList.search_node(23), 65)
myList.print_list() # [43] ==> [15] ==> [10] ==> [23] ==> [65]
print("=========================")
myList.delete_from_start()
myList.delete_from_last()
myList.delete_node(10)
myList.print_list() # [15] ==> [23]

print("=========================")
for i in myList:
    print(f"[{i}]", end=" ==> ") # [15] ==> [23] ==>