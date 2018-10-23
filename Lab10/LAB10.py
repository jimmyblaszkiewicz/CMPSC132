#Lab #10
#Due Date: 10/26/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz 
# Collaboration Statement: I completed this assignment by myself
#                          using only the class materials
#                          using only the class materials
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None
        self.length = 0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self.length

    def enqueue(self, value):
        # if no elements in queue yet, set new node = head and tail
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        # if there are elements, put new node as tail.next and reset tail to new node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    def dequeue(self):
        # if queue is already empty, say so
        if self.isEmpty():
            return 'Queue is empty'

        # set dequeued temp variable to head, set new head to the next item in queue
        dequeued = self.head
        self.head = dequeued.next
        
        # if dequeued was also the tail, set tail to none
        if self.length == 1:
            self.tail = None

        # unlink dequeued from queue and decrement length
        dequeued.next = None
        self.length -= 1
        return dequeued.value
