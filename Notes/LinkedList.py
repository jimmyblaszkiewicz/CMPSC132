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

    def __str__(self):
        return 'Node({})'.format(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    @property
    def isEmpty(self):
        # if list is empty then there is no head
        return self.head == None
    
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
            self.length += 1

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


    def __repr__(self):
        current = self.head

        out = []
        while current:
            out.append(str(current.value))
            current = current.next

        out=' '.join(out)
        return "Head:{}, Tail:{}\nList:{}".format(self.head, self.tail, out)

    __str__ = __repr__

    def __getitem__(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current=current.next                

        return None

    def __delitem__(self, value):
        # no items in list at all
        if self.isEmpty:
            return 'List is empty'

        # one item in list
        if len(self) == 1:
            if self.head.value == value:
                self.head = None
                self.tail = None
            else:
                return 'Node is not in the list'

        # multiple items in list
        else:
            current = self.head
            previous = None
            found = False

            # walk through the list setting previous and current
            while current is not None:
                if current.value == value:
                    found = True
                    break
                previous = current
                current = current.next

            # item not in the list
            if not found:
                return 'Node not in the list'

            # if we are deleting the head
            if previous == None:
                self.head = current.next
                current.next = None
            # elif we are deleting the tail
            elif current.next == None:
                previous.next = None
                self.tail = previous
            # something in the middle of the list
            else:
                previous.next = current.next
        
        self.length -= 1


    # add a node to the end of the list
    def append(self, e):
        new_node = Node(e)

        if self.isEmpty:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # set new node to be the next of whatever the current final node is
        self.tail.next = new_node
        self.tail = new_node
        self. length += 1

    def insert(self, after, value):
        insert_after = self[after]
        if insert_after is None:
            return 'Item is not in list'

        newNode = Node(value)
        newNode.next = insert_after.next
        insert_after.next = newNode

        if newNode.next is None:
            self.tail = newNode

        self.length += 1


    def reverse(self):
        if self.isEmpty:
            return 'List is empty'

        current = self.head
        previous = None

        self.head, self.tail = self.tail, self.head
        while current is not None:
            oldnext = current.next
            current.next = previous
            previous = current
            current = oldnext


if __name__ == '__main__':
    x = LinkedList()
    x.append(4)
    x.add(3)
    x.add(2)
    x.append(5)
    print(x)
    print(x)
    x.reverse()
    print(x)
    print('Length = {}'.format(x.length))