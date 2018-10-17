#Lab #9
#Due Date: 10/19/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program by myself,
# using only the class materials.
# 
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    '''
        Creates an empty Stack with support for push and pop operations
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
        self.length = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    @property
    def isEmpty(self):
        # if the stack does not have a top it is empty
        return self.top is None


    def __len__(self):
        return self.length
    
    def peek(self):
        if self.isEmpty:
            return 'Stack is empty'

        return self.top.value

    def push(self,value):
        # create new_node from value
        new_node = Node(value)
        # set current top to next of new node
        new_node.next = self.top
        # set new top to new node
        self.top = new_node

        self.length += 1

    def pop(self):
        if self.isEmpty:
            return 'Stack is empty'

        # temporary variable for current top to be popped
        popped = self.top
        # set new top to the one after popped and unlink popped
        self.top = popped.next
        popped.next = None

        self.length -= 1
        return popped.value