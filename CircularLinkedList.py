class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next
        
class CircularLinkedList:
    def __init__(self, last=None) -> None:
        self.last = last
        
    def is_empty(self) -> bool:
        return self.last == None
    
    def search_node(self, data) -> Node:
        '''
            - If list is empty then return None
            - Assign the reference of first node to temp pointer
            - Traverse the list until the temp pointer is the last node and if data found then return that node
            - If loop completes and no data found then check for the last node and if data found then 
                return the last node
        '''
        if self.is_empty():
            return None
        
        temp = self.last.next
        while temp is not self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    
    def print_list(self) -> None:
        if not self.is_empty():
            temp = self.last.next
            while temp is not self.last:
                print(f"[{temp.item}]", end=" ==> ")
                temp = temp.next
            print(f"[{temp.item}]")
        else:
            print("There are no any node available in the list !")
            
    def insert_at_start(self, data) -> None:
        '''
            - Create a new node with data
            - If list is empty then assign the reference of new node to new node itself
            - Assign the reference of new node to last pointer
            - If list is not empty then assign the reference of next node of last node (first node)
                to next reference of new node
            - Assign the reference of new node to next node of last node (first node --> second node)
        '''
        node = Node(data)
        if self.is_empty(): # Empty List
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node
            
    def insert_at_last(self, data) -> None:
        '''
            - Create a new node with data
            - If list is empty then assign the reference of new node to new node itself and
                assign the reference of new node to last pointer
            - If list is not empty then assign the reference of next node of last node (first node) to 
                reference of new node
            - Assign the reference of new node to next node of last node (first node --> second node) 
                as well as to last pointer
        '''
        node = Node(data)
        if self.is_empty():
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node
            
    def insert_after_node(self, temp, data):
        '''
            - Create a new node with data and reference of next reference of temp pointer to new node
            - Assign the reference of new node to next reference of temp pointer
            - If temp pointer is the last node then assign the reference of new node to last pointer
        '''
        if temp is not None:
            node = Node(data, temp.next)
            temp.next = node
            if temp is self.last:
                self.last = node
    
    def delete_from_start(self) -> None:
        '''
            - If list has only one node then assign the reference of last node to None 
                otherwise assign the next to next reference of last node (second node) to next reference 
                of last node (first node)
        '''
        if not self.is_empty():
            if self.last.next is self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
    
    def delete_from_last(self) -> None:
        '''
            - If list has only one node then assign the reference of last node to None 
                otherwise traverse the list until temp pointer is the second last node then
                assign the next reference of last node (first node) to next reference of temp pointer
                after that assign the temp pointer to last node
        '''
        
        if not self.is_empty():
            if self.last.next is self.last:
                self.last.next = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp