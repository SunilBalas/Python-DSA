class Node:
    def __init__(self, item=None, left=None, right=None) -> None:
        self.item = item
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root
    
    def insert_data(self, data) -> None:
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            temp = self.root
            while True:
                if data < temp.item:
                    if temp.left is None:
                        temp.left = node
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node
                        break
                    temp = temp.right
    
    def search_node(self, data) -> Node:
        if self.root is None:
            return None
        else:
            temp = self.root
            if temp.item == data:
                return temp
            
            while True:
                if temp is not None:
                    if data < temp.item:
                        if temp.item == data:
                            return temp
                        temp = temp.left
                    else:
                        if temp.item == data:
                            return temp
                        temp = temp.right
                else:
                    return None
    
    def inorder_traversal(self) -> None:
        if self.root is None:
            print("There are no nodes available in the given tree !")
        else:
            # TODO: Need to check for the inorder traversal
            pass

tree = BinarySearchTree()
tree.insert_data(10)
tree.insert_data(-5)
tree.insert_data(50)
tree.insert_data(98)
tree.insert_data(65)
tree.insert_data(-20)
tree.insert_data(5)
tree.search_node(-5)