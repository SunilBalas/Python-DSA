# Data Structures and Algorithms using Python

## Linear Data Structures
- ### Linked List
  - A Linked List is a linear data structure where elements are stored in nodes, and each node points to the next one in the sequence. The last node points to null to indicate the end of the list.

    **1. Singly Linked List**
      - In a Singly Linked List, each node has a data element and a single reference (link or pointer) to the next node in the sequence.

    **2. Doubly Linked List**
      - A Doubly Linked List is similar to a singly linked list, but each node contains two pointers: one pointing to the next node and another pointing to the previous node.

    **3. Circular Singly Linked List**
      - A Circular Singly Linked List is a variation of a singly linked list where the last node points back to the first node, forming a circle.

    **4. Circular Doubly Linked List**
      - Similar to the circular singly linked list, a Circular Doubly Linked List has nodes with two pointers, but in this case, each node has a link both to the next and the previous node, forming a circular structure.

- ### Stack
  - A Stack is a collection of elements with two main operations: push (to add an element) and pop (to remove the most recently added element). It follows the Last In, First Out (LIFO) principle.

- ### Queue
  - A Queue is a collection of elements with two main operations: enqueue (to add an element) and dequeue (to remove the element at the front). It follows the First In, First Out (FIFO) principle.

    **1. Deque (Double Ended Queue)**
      - A Deque (Double Ended Queue) is a generalization of a queue where elements can be added or removed from both ends, providing more flexibility than a regular queue.

    **2. Priority Queue**
      - A Priority Queue is a queue where elements have associated priorities, and the element with the highest priority is served before others. It does not follow the strict FIFO order.

## Recursion
  - Recursion is a programming concept where a function calls itself in its definition. Recursive functions break down a problem into smaller sub-problems and solve them.

## Non-Linear Data Structures
- ### Tree
  - A Tree is a hierarchical data structure with a root node and branches that connect to other nodes. Each node has child nodes, forming a tree-like structure.

    **1. Binary Search Tree (BST)**
      - A Binary Search Tree (BST) is a binary tree where the left child of a node contains elements smaller than the node, and the right child contains elements larger than the node. This ordering property makes searching efficient.

- ### Graph
  - Graphs in data structures are used to represent the relationships between objects. Every graph consists of a set of points known as vertices or nodes connected by lines known as edges. The vertices in a network represent entities.

    **1. Breadth First Search (BFS)**
      - BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of the graph) and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

    **2. Depth First Search (DFS)**
      - DFS is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of the graph) and explores as far as possible along each branch before backtracking.

## Sorting
- ### Bubble Sort
- ### Modified Bubble Sort
- ### Selection Sort
- ### Insertion Sort
