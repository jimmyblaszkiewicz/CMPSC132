# Queue implementation using a Python List
class Queue:
    def __init__(self):
        self.items = []

    @property
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

    @property
    def isEmpty(self):
        return self.root is None
    
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

    def breadthFirstSearch(self):
        if self.isEmpty:
            return 'Tree is Empty'

        q = Queue()
        visited = []
        # root first
        q.enqueue(self.root)
        # get loopy
        while not q.isEmpty:
            node = q.dequeue()
            visited.append(node.value)

            # Left
            if node.left is not None:
                q.enqueue(node.left)

            # right side
            if node.right is not None:
                q.enqueue(node.right)

        return visited


    def preorder(self, node):
        # visit entire tree by calling mytree.preorder(mytree.root)
        # start with node (preorder is recursive)
        if node is not None:
            # preorder = root left right
            # print node and trailing ' '
            # can just as easily be appending to a string to return at the end
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        # similar to preorder (just different order)
        if node is not None:
            # inorder = left root right
            self.inorder(node.left)
            print(node.value, end = ' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            # postorder = left right root
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.value, end = ' ')
