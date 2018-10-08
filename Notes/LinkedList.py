'''
Linked List Implementation
Jimmy Blaszkiewicz
CMPSC 132
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # for doubly linked list need previous pointer
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    @property
    def isEmpty(self):
        # if list is empty then there is no head
        return self.head == None:
    
    # override len method common to all lists
    def __len__(self):
        return self.length

    def size(self):
        return self.length
    
    def add(self, value):
        new_node = Node(value)

        if self.isEmpty:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1


    def __contains__(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False
        
    def delete(self, e):
        # make a temp node from head
        temp = self.head

        if temp is not None:
            if temp.value == e:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.value == e:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return 'key not found in list'

        prev.next = temp.next
        temp = None

    # add a node to the end of the list
    def add_last(self, e):
        new_node = Node(e)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete_first(self):
        if self.isEmpty:
            return 'The list is empty'

        self.head = self.head.next
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # add to beginning of list
    def add_first(self, e):
        new_node = Node(e)
        # because its at the beginning next is the current head
        new_node.next = self.head

        # change previous of head to the new_node to link backwards
        if self.head is not None:
            self.head.prev = new_node

        # set the new head to the new node
        self.head = new_node

