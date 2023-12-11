from typing import Any, List

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
    
    def find_min_value_node(self) -> Any:
        if self.root is not None:
            return self.recursive_find_min_value_node(self.root)
    
    def recursive_find_min_value_node(self, root) -> Any:
        if root.left is None:
            return root.item
        return self.recursive_find_min_value_node(root.left)
    
    def find_max_value_node(self) -> Any:
        if self.root is not None:
            return self.recursive_find_max_value_node(self.root)
    
    def recursive_find_max_value_node(self, root) -> Any:
        if root.right is None:
            return root.item
        return self.recursive_find_max_value_node(root.right)
    
    def get_tree_size(self) -> int:
        result = self.inorder_traversal()
        return len(result)
    
    def delete_node(self, target) -> None:
        if self.root is not None:
            if self.root.left is None and self.root.right is None:  # Only one node present in the tree
                self.root = None
            else:
                parent = self.root
                self.recursive_delete_node(self.root, parent, target)
    
    def recursive_delete_node(self, root, parent, target):
        if target < root.item:
            parent = root
            self.recursive_delete_node(root.left, parent, target)
        elif target > root.item:
            parent = root
            self.recursive_delete_node(root.right, parent, target)
        else:
            '''
                TODO: Need to check if targeted node has how many children ?
                    1. Targeted node has no child
                    2. Targeted node has one child
                    3. Targeted node has two children
            '''
            pass


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
print(f"Min value item node: {tree.find_min_value_node()}")
print()
print(f"Max value item node: {tree.find_max_value_node()}")
print()
print(f"Tree Size: {tree.get_tree_size()}")
