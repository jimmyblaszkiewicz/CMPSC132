#HW 5
#Due Date: 12/07/2018, 11:59PM
########################################
#
# Name: James Blaszkiewicz
# Collaboration Statement: I completed this program using only the class materials.
#
########################################

# ---Copy your code from labs 9 and 10 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "{}".format(self.value) 

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
    
    @property
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

    @property
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'

        return self.head


#----- HW5 Graph code     
class Graph:
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:self.vertList = graph_repr


    def addVertex(self,key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList


    def addEdge(self,frm,to,cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))
        return self.vertList


    def bfs(self, start):
        # Your code starts here
        if start not in self.vertList:
            return 'error: start node not in graph'
        
        # create visited dict with all set to False
        visited = {}
        for i in self.vertList:
            visited[i] = False

        # create queue and append start note, mark start node as visited
        q = Queue()
        q.enqueue(start)
        visited[start] = True

        # create list to hold output of bfs
        bfs_out = []

        
        # while there are items in the queue
        while q:
            # loop through a sorted list of attached neighbors to first item in queue
            for i in sorted((self.vertList[str(q.peek)])):
                # if these neighbors have not been visited then add them to the queue
                # and mark them visited

                # weighted edge
                if type(i) == tuple:
                    if not visited[i[0]]:
                        q.enqueue(i[0])
                        visited[i[0]] = True

                # non-weighted edge
                elif not visited[i]:
                    q.enqueue(i)
                    visited[i] = True

            # append the first item in the queue to the bfs output
            bfs_out.append(q.dequeue())

        return bfs_out


    def dfs(self, start):
        # Your code starts here
        if start not in self.vertList:
            return 'error: start node not in graph'
        # create stack to hold vertices during transit
        s = Stack()

        # create visited list to keep track of visited vertices
        # visited will also be the output
        visited = []

        # put the starting vertex at bottom of stack and mark it as visited
        s.push(start)
        visited.append(start)
        
        while s:
            # take the alphabetically first vertex connected to s.peek
            for i in sorted(self.vertList[str(s.peek)]):
                # weighted graph
                if type(i) == tuple:
                    # if i not yet visited, push to stack and add to visited
                    if i[0] not in visited:
                        s.push(i[0])
                        visited.append(i[0])
                        # then exit the for loop immediately
                        break

                # non-weighted graph dont have to deal with tuples
                elif i not in visited:
                    s.push(i)
                    visited.append(i)
                    # then exit the for loop immediately
                    break

            # using for->else to check if the loop didn't exit on an explicit break
            else:
                # if all neighbors for top of stack already in visited
                # pop top of stack
                s.pop()

        return visited


    ### EXTRA CREDIT, uncomment method definition if submitting extra credit
    
    def dijkstra(self,start):
        # Your code starts here
        if start not in self.vertList:
            return 'error: start node not in graph'

        # use queue to track vertices
        q = Queue()

        # use visited list to track visited vertices
        visited = []

        paths = {}
        for i in self.vertList:
            # initialize minimum path lengths to infinity
            paths[i] = float('inf')

        # set smallest path to start to 0
        paths[start] = 0
        q.enqueue(start)

        while q:
            vertex = str(q.dequeue())
            # for each connected neighbor to the current vertex...
            for i in self.vertList[vertex]:
                # check if the edge is weighted at all
                if type(i) != tuple:
                    if i not in visited:
                        visited.append(i)
                        q.enqueue(i)
                    # treat unweighted edges as weight 1
                    if paths[i] > paths[vertex] + 1:
                        paths[i] = paths[vertex] + 1            

                    # dont execute the code for tuples down below
                    continue

                # if the node has not appeared yet in visited
                if i[0] not in visited:
                    # enqueue the new neighbor and append to visited
                    visited.append(i[0])
                    q.enqueue(i[0])

                # check if the new path is less than the current path
                if paths[i[0]] > paths[vertex] + i[1]:
                    #shortest path from start to the current vertex + current vertex to neighbor
                    paths[i[0]] = paths[vertex] + i[1]

        return paths