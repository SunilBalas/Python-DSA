from typing import List

class Node:
    def __init__(self, item=None, left=None, right=None) -> None:
        self.item = item
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root
    
    def insert_node(self, data) -> None:
        self.root = self.recursive_insert_node(self.root, data)
    
    def recursive_insert_node(self, root, data) -> Node:
        if root is None:
            return Node(data)
        
        if data < root.item:
            root.left = self.recursive_insert_node(root.left, data)
        elif data > root.item:
            root.right = self.recursive_insert_node(root.right, data)
        
        return root
    
    def search_node(self, data) -> Node:
        return self.recursive_search_node(self.root, data)
    
    def recursive_search_node(self, root, data) -> Node:
        if root is None or root.item == data:
            return root
        
        if data < root.item:
            return self.recursive_search_node(root.left, data)
        elif data > root.item:
            return self.recursive_search_node(root.right, data)
    
    def inorder_traversal(self) -> List:
        result = []
        self.recursive_inorder_traversal(self.root, result)
        return result
    
    def recursive_inorder_traversal(self, root, result) -> None:
        if root:
            self.recursive_inorder_traversal(root.left, result)
            result.append(root.item)
            self.recursive_inorder_traversal(root.right, result)
    
    def preorder_traversal(self) -> List:
        result = []
        self.recursive_preorder_traversal(self.root, result)
        return result
    
    def recursive_preorder_traversal(self, root, result) -> None:
        if root:
            result.append(root.item)
            self.recursive_preorder_traversal(root.left, result)
            self.recursive_preorder_traversal(root.right, result)
    
    def postorder_traversal(self) -> List:
        result = []
        self.recursive_postorder_traversal(self.root, result)
        return result
    
    def recursive_postorder_traversal(self, root, result) -> None:
        if root:
            self.recursive_postorder_traversal(root.left, result)
            self.recursive_postorder_traversal(root.right, result)
            result.append(root.item)


tree = BinarySearchTree()
tree.insert_node(10)
tree.insert_node(-5)
tree.insert_node(50)
tree.insert_node(98)
tree.insert_node(65)
tree.insert_node(-20)
tree.insert_node(5)
tree.search_node(-5)

print(f"{tree.inorder_traversal()}")
print()
print(f"{tree.preorder_traversal()}")
print()
print(f"{tree.postorder_traversal()}")
print()
