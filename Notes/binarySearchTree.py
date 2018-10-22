# Queue implementation using a Python List
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Binary Search Tree implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
                
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        # to be used like mytree.insert(mytree.root, 4)

        # if no root, make the value the new root
        if node is None:
            # this code won't be run if insert is called again down below
            # because it checks if that left/right was none
            self.root = Node(value)

        else:
            # if value is less than or equal to 'root'
            if value <= node.value:
                if node.left is None:
                    # if theres nothing on the left just add it there
                    node.left = Node(value)
                else:
                    # otherwise run insert again with that node 
                    # (bc binary search trees are made of other binary search trees)
                    self.insert(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)