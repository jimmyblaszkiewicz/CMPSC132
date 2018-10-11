#Lab #8
#Due Date: 10/12/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program by myself 
# using only the class materials             
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        Creates a linked list in ascending order
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(8)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> print(x)
        Head:Node(-6)
        Tail:Node(8)
        List:-6 3 7 8
        >>> len(x)
        4
        >>> x.pop()
        8
        >>> print(x)
        Head:Node(-6)
        Tail:Node(7)
        List:-6 3 7
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        # add new attribute length to avoid looping through entire
        # list every time we need the length
        self.length = 0


    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head, self.tail, out))


    __repr__=__str__


    def __len__(self):
        # write your code here
        # use class attribute rather than looping through entire list
        # self.length maintained in other methods
        return self.length

    
    @property
    def isEmpty(self):
        # write your code here
        # if self.head is None - the list is empty
        # otherwise it is not
        return self.head is None


    def add(self, value):
        # write your code here
        new_node = Node(value)
        # if list is empty, just add new node as head and tail
        if self.isEmpty:
            self.head = new_node
            self.tail = new_node
            return

        # otherwise find correct spot in current list
        # new_node will be inserted before current and after previous
        current = self.head
        previous = None
        while current:
            if current.value > new_node.value:
                # if we find a value greater than our new value
                # stop looping
                break
            # increment current and previous
            previous = current
            current = current.next
            

        # insert new node before current head (previous is None)
        if current == self.head:
            self.head = new_node
            new_node.next = current
        
        # insert new node at the end of the list
        # bc current is now past the tail (current is None)
        elif previous == self.tail:
            self.tail = new_node
            previous.next = new_node

        # otherwise put new node after previous and before current
        else:
            new_node.next = current
            previous.next = new_node

        self.length += 1

    
    def pop(self):
        # write your code here
        # if the list is empty, give message
        if self.isEmpty:
            return 'List is empty'

        current = self.head
        previous = None

        while current:
            # if we reach the end of the list
            if self.tail == current:
                # if the head is equal to the tail (1 item list)
                if self.head == current:
                    self.head = None
                    self.tail = None
                    break

                # otherwise unlink current from previous.next
                # set previous as new tail and break
                previous.next = None
                self.tail = previous
                break

            # increment previous and current
            previous = current
            current = current.next

        self.length -= 1
        return current.value