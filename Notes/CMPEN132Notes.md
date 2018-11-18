

#Intro to Python
  - high level
  - GEN PURPOSE
  - Interpreted
    - Dynamic
    - Emphasizes code readability, simple syntax
       - Java has complex syntax in hello world program with all that public static void main nonsense
       - Python is just: print(“Hello World”)
       - Uses whitespace indentation rather than curly braces or keywords to delimit blocks
       - This is a huge problem i hate it
       - Game breaking
    - Cross platform

###Dynamic language
   - Static - variable name attached to object and type, when changes are made, makes sure that type matches initial type
   - Dynamic - more freedom on working with data, type doesn’t have to match after initialization (actually no type is given in initialization)

###About the python program
####Two kinds of programs to process high level languages into low level languages
   - Interpreters: Source code > interpreter > output
Translates line by line
      - Better for testing for running quickly
   - Compilers: Source code > Compiler > Object Code > Executor > Output
      - Translates entire code before running, but makes an executable file to run instantly
      - Slower to run multiple times quickly

####Interpreting Python Programs

#####What Happens when we enter python hello.py at the command shell prompt
   - Python tells the OS to load the Python interpreter into memory and run it
   - We invoke python with a command line argument which python reads after it starts running
   - Since the command line argument was the name of a file (hello.py) the python loads the file named by the argument and executes the Python code in it
   
#####Python Interpreter
######Two ways to use the python interpreter
   - Shell mode: type python expressions into the python shell, and the interpreter immediately shows the result

   - Python Shell
   - REPL
   - Invoke the python interactive shell by entering python at your command shell’s prompt

---

#Python Syntax
####Variables
   - Cannot start a name with a number
   - Need to initialize the variable before it’s referenced
      - x=x+3 wont work unless x was defined earlier
   - Can change types
   - Creates a memory block every time we create a value

####Mutable and immutable objects
   - Mutable objects: can be altered in place
      - Byte array
      - list 
      - Set
      - Dict
      - User-defined classes (unless specifically made immutable)
   - Immutable objects: cannot be changed in place (in the same memory allocation)
      - Int
      - Float
      - Long
      - Complex
      - String
      - Bytes
      - Tuple
      - Range
      - Frozen set (immutable version of set)
      - Boolean
      - Array

#####Aliasing
   - Occurs when two or more variables reference the same object

####String Methods
   - Str is a class with many methods that can be invoked using the dot operator
   - `str.find(substr)` returns the index of the first occurrence of substr in str:

```python
>>> “Hello world”.find(‘l’)
2
>>> ”banana”.find(“nan”)
2
```

   - `str.replace(old, new)` returns a copy of str with all occurrences of old replaced with new

```python
>>>”banana”.replace(“ba”,”Choco”)
‘Choconana’
```

   - Check documentation to see if you need more arguments to specify 
`str.split(delimiter)`

```python
>>>”banana”.split(“nan”)
[‘ba’, ‘a’]
```

   - `str.join(iterable)` returns a string that is the concatenation of all the elements of iterable with str in between each element

```python
“co”.join([‘cho’,’late’])
chocolate
“”.join([‘cho’,’co’,’late])
chocolate
```

   -  `str.strip()` returns a copy of str with leading and trailing whitespace removed
```python
>>>” spaces       “.strip()
‘Spaces’
```

   - `str.upper()` returns a copy of the string with all lowercase characters in uppercase
   - `str.isupper()` returns `True` if str is all uppercase
   - `str.isdigit()` returns `True` if str is all digits
   - `str.startswith(substr)` returns `True` if str starts with substr

####List Operators
   - The in operator tests for list membership. Can be negated with not
```python
>>> numbers = [1,2,3,4,6,7,8,9]
>>>5 in numbers
False
>>>6 in numbers
True
```
   - The + operator concatenates two lists 
   - The * operator repeats a list, producing a new list
   - `len(s)` returns the number of elements in the list
   - `min(s)` returns the least element of s, max(s) returns the greatest
   - `sorted(s)` returns a new sorted list
   - _Returns **not** changes_
   - `s.count(x)` number of occurences of x in the sequence s
   - `s.append(x)` adds the single element x to the end of s
   - `s.extend(x)` adds the elements of x to the end of the list s
   - `s.remove(x)` removes the first occurence of x in s, or raises an error if x is not in s
   - `s.pop()` removes and returns the last element of th list
      - _List **is** modified_
   - `s.join()` combines the elements of a list to form a string
   - `s.sort()` modifies the list it is invoked on

####Lists - Append versus Concatenate
   - With append the original list is simply modified
   - With concatenation, an entirely new list is created

####Sequence traversal

```python 
Ice_cream = [‘chocolate’, ‘vanilla’, ‘mint’, ‘strawberry’]
```
   - By item or by index

```python
for flavors in ice_cream:
   print(flavors)

for position in range(len(ice_cream)):
   print(ice_cream[position])
```

__Remember__

   - Carefully name your identifiers so you can create readable programs
   - Python programs make extensive use of built-in methods and data types and often combine them (lists of lists, dictionaries of lists, etc)

####`True` in Python
   - Most things evaluate to true, except false things

#### Writing and running a python script
   - Write a function that takes a string as an argument and returns the username from an email address

```python
def username(email):
   return email[:email.find('@')]
```


######8/29/18
####For statement
   - Iteration statement

```python
for variable in sequence:
```

####While statement
   - While loop repeatedly executes a target statement as long as a given condition is true
   - Can result in infinite loops if condition is not falsified

####Break statement
   - Break terminates execution of a loop
   - Can be used in both while and for loops

####Continue statement
   - Continue causes to immediately skip the processing of the rest of the body of a loop for the current iteration
   - The loop still carries on running for its remaining iterations
   - Can be used in both `for` and `while` loops


#Errors Debugging and Testing
##Errors
###Different kinds of errors can occur in a program, and it is useful to distinguish among them to track them down more quickly
   - Syntax errors: produced by Python when it is translating the source code into bytecode
   - Runtime errors: produced by the runtime system if something goes wrong while the program is running
   - Semantic errors: problems with a program that compiles and runs but does not do the right thing

####Syntax Errors: usually easy to fix once we find them
   - Error messages are often not helpful
      - `Invalid syntax`
      - `Invalid token`
      - `Unexpected indent`
   - Error message _does_ tell us where in the program the problem occurred

#####Avoiding Syntax Errors
   - Make sure you are not using a keyword for a variable name
   - Check that you have a colon at the end of the header of every compound statement including `for`, `while`, `if`, and `def`
   - Check that indentation is consistent
   - Don't mix tabs and spaces
   - Make sure that any strings in the code has matching quotation marks
      - Kind of hard to screw that up 
   - Make sure you do not have an unclosed bracket
   - Check for classic = rather than == inside a conditional

#### Runtime Errors
   - Program does absolutely nothing
   - Program hangs
   - Infinite loop
   - Infinite recursion
   - When i run the program i get an exception such as:
      - NameError
      - TypeError
      - KeyError
      - AttributeError
      - IndexError
   - Make sure you test all your code, including random else block

#### Semantic Errors
   - Hardest to debug because compiler and runtime system provide no information about why
   - Code will run successfully in the sense that the computer will not generate any error messages. However the program will not do the right thing.

## Software Development lifecycle
Requirements -> Design -> Coding -> Debugging Testing -> Deployment -> Req…
Debugging
   
   - Involves locating and correcting code errors in program
   - Begins when you start writing code and continues as code is combined with other units of programming
   - Best place is away from the computer
   - Can be more time consuming than writing it, but its the most efficient way to test and make sure it works correctly

###6 stages of debugging
   1. That can’t happen
   2. That doesn’t happen on my machine
   3. That shouldn’t happen
   4. Why does that happen?
   5. Oh, I see,
   6. How did that ever work?

####Principles
   - Know what the code is supposed to do
   - When in doubt, print to the console
   - Make it fail every time
   - Change one thing at a time
   - Keep track of what you have done
   - Do not panic when you generate a ton of errors
   - Version control revisited
   - Ask for help

######8/31/18
##Advantages of Unit Testing
Can write down several test cases and let them be checked every time we make changes to our code - without retesting every time
  
   - Most popular is unittest module
   - Create a class that inherits from the unittest.TestCase class

```python
import unittest
from script import my_function
class MyTest(unittest.TestCase):
   def test_my_function(self):
      self.assertEqual(my_function(input),expected_output)


If __name__==’__main__’: unittest.main(exit=False)
```

   - Based on assertions
      + like assertTrue
      + assertEqual
      + others

---
######9/10/18
#OOP = Object Oriented Programing
##What are objects
###Object construction
   - When calling a new class
   - New instance of that class is created
   - The `__init__ method (constructor, initializer)` is called with the new object as its first argument, by convention named `self`, along with any additional arguments provided in the call expression

```python
class Account:
   def __init__(self, name):
      self.holder=name
      self.balance=0

```

   - `__new__` is responsible for controlling the creation of the object
      - Sometimes maybe you don’t want the object to be created under certain conditions who knows

####The `self`
   - Refers to the object itself
   - If you have a method which takes no arguments, then you still have to have the self argument
   - binds the instructions in the method call with the object
   - 1 class but many objects with their own states

###Object identity
####Creation
   - Every object that is an instance of a user defined class has a unique identity

```python
x=Account(‘Alan’)
y=Account(‘Liz’)
```

   - Class is just a template, object holds all the info

```python
>>>x.holder
‘Alan’
>>>y.holder
‘Liz’
```

   - The identity operator ‘is’ checks to see if two expressions evaluate to the same object
      - The same exact memory block
   - Binding an object to a new identifier using the assignment operator does not create a new object
      - Instead Gives another name to the same object

```python
x=Account(‘Alan’)
W = x
>>> w is x
True
```

####Attributes

```python
class Dog:
   def __init__(self, name, breed):
      self.name = name
      self.breed = breed
      self.vaccines = 0
   def getVaccine(self):
      self.vaccines+=1
      return self.vaccines
```

```python
>>> Harry = dog(‘harry’, ‘chihuahua’)
>>> harry.vaccines
0
>>> getattr(harry, ‘vaccines’)
0
>>>harry.getVaccine()
1
>>>harry.vaccines
1
>>>hasattr(harry, ‘vaccines’)
True
>>>hasattr(harry, ‘size’)
False
```

####Class and instance attributes
   - Different name, breed and such for each dog object instance

```python
class Dog:
index = 0.04
   def ___init___ ...
```

   - Look at constructor for index, no, look at class
   - Index is not copied to each instance, it belongs to the class

#####Attribute assignment
   - Assigment statements with dot expression affect attr for the object on the left-hand of the dot expression
   - If its an instance, then assignment sets instance attr
   - If object is a class, then assignment sets a class attribute

```python
>>>Harry.index = .09
#Creates an attribute index into Harry object
>>>Harry.index
.09
>>>Liz.index
.04
>>>Dog.index = .07
Harry.index
.09
```

###Special methods and operator overwriting
   - Special methods have double underscores at the beginning and end
   - You do not have to invoke them directly. The invocation is realized behind the scenes
   - Print obj goes to `__str__()`

```python
__str__(self):
   return ‘My name is {}’.format(self.name)
```

###Inheritance
   - Arrange objects in a hierarchy from most general to most specific
   - Classes can extend the definition of other classes
   - Allows use (or extension) of methods and attributes already defined in the previous one


To define a subclass, put the name of the superclass in parentheses after the subclass’s name on the first line of the definition.

```python
class George (Human):
```

   - Superclass has all the common functionality for the subclasses
Subclass inherits from the superclass
   - Not the other way around
   - Superclass is more general
   - Subclass more specific
   - `Animal` is a superclass
   - Mammal is subclass of animal and superclass of Dog and Zebra
   - Lizard is parent class of iguana and subclass of Reptile

```python
class name(parent):
   body
```

   - Need to initialize other values (name and vaccines for instance)
   - Use `super().__init__(name)`
   - Initializes name and vaccines (vacc initially 0)

###Polymorphism
   - Based on greek words for many forms
   - Process of using an operator or function in different ways for data input
   - Can be carried out through inheritance 


   - “Speak everybody”
      - `Quack, moo, woof, hiss, blub-blub`
   - Same command sent, but different result

```python
3+4
>>> 7
‘3’+’4’
>>>’34’
```

   - Same operator but different result

###Encapsulation
   - Restrict access to methods and variables to prevent the data from being modified by accident
   - Prevents from accessing accidentally, but not intentionally
   - Private attributes and methods are not really hidden, they are renamed `_ClassName__VariableName` 

   - Access private variables with set methods

```python
def setMaxSpeed(self, speed):
    self.__maxspeed = speed
    return self.__maxspeed
def getMaxSpeed(self, speed):
    return self.__maxspeed
```


###Data Abstraction
   - Abstract classes contain one or more abstract methods
   - May not be instantiated and require subclasses to provide implementations for the abstract methods
   - Abstract methods are methods that are declared but contain no implementation

####Data Abstraction with ABC
How do you force the subclasses to implement the abstract methods?

   - Subclass behaves like parent class + something
   - Every class that inherits from me must have these methods

```python
from abc import *
class Vehicle(ABC):
   def __init__(self, name):
      super().__init__()
      self.name=name

   @abstractmethod
   def drive(self):
      Raise NotImplementedError("Subclass must implement abstract method")

class MiniVan(Vehicle):
    def __init__(Self, name, seats):
        super().__init__(name)
        self.seats = seats
    def drive(self):
        return 'Mini Van driving - baby on board!'
    def stop(self):
        return 'Mini van stopping'

```

---
######9/24/18
#Midterm things
   - Date 09/28 - 09/29
   - Location Thomas 101
   - Scope: Modules 1-4
   - In class: Paper exam (80%): 14 questions
      - 6 multiple choice
      - 4 open ended
      - 2 predict the output
      - 2 writing code
   - Coding Exam (20%): Write 3 programs
      - due saturday night

---

#Recursion
##What is Recursion
   - method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a point where it can be solved trivially
   - recursive functions call themselves
   - must have a termination condition, often called base case. this is necessary to stop the function from calling itself an infinite number of times
      - Python might be around 500 max function calls

###Laws of Recursion
####All recursive algorithms must obey three important laws
    -must have a base case
    -must change its state and move toward the base case
    -must call itself, recursively
        -haha the laws of recursion are recursive, hilarious.

##Sum a list of numbers


```python
def listsum(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

def recursiveSum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursiveSum(numbers[1:])
```

######9/26/18
## Harmful Recursion
   - When used incorrectly, recursion could take too much memory and computer resources

### Fibonacci numbers: 

#### Recursively

```python
def fibr(n):
   if n <= 1:
      return n
   else:
      return fibr(n-1) + fibr(n-2)

fibr(5)
```

   - when the recursion tree is drawn, the same value is calculated many many times
   - `fibr(5)` takes 15 open frames to calculate

#### Iteratively

```python
def fibi(n):
   x, y = 0,1
   for i in range(n):
      x, y = y, x + y
   return x
```

|Pros                       | Cons                      |
|---------------------------|---------------------------|
|elegant                    | hard logic                |
|complex -> simple          | memory and time intensive |
|sequence generation easier | hard to debug             |

Table: Pros and Cons of Recursion

---

###### 10/1/18
# Abstract Data Types
 Abstract Data types are logical descriptions of how we view the data and the operations that are allowed without regard to how they will be implemented
 
 We are only concerned with what the data is representing and not with how it will eventually be constructed.

### Data Structure
   - A data structure is the implementation of an abstract data type that requires a physical view of the data using some collection of programming constructs and primitive data types
   - A way of organizing and storing data so that _operations_ can be performed efficiently
      + inserting
      + deleting
      + accessing
      + finding
      + sorting...
   - not all of them perform super efficiently

### Memory Allocation
Not a nice huge chunk of memory where everything is right next to eachother

   - something links the memory blocks together for a list

### Nodes
   - value|next------> value|next ------> value|next -------> value|next
   - each value|next is a `Node`

```python
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

```

```python
# set up the main list
>>> a=Node(8)
>>> b=Node(2)
>>> c=Node(6)
>>> d=Node(4)
```

```python
# connect the Nodes
>>> b.next=d
>>> d.next=c
>>> c.next=a
```

```python
# now everything is connected, now we should print out the 'list'
>>> current = b
>>> while current:
...     print(current.value, end= ' ')
...     current=current.next
...
2 4 6 8

```

##Linked Lists
### Linear Structures
   - Stacks queues and linked lists are examples of data collections whose items are ordered depending on how they are added or removed
   - Linear structures can be though of as having two ends, sometimes these ends are the 'left' and 'right' or sometimes the 'head' and 'tail'
   - What distinguishes one from the other is the way in which items are added and removed, in particular the location where these additions and removals occur.
   - These variations give rise to some of the most useful data structures in computer science. they appear in many algorithms and can be used to solve a variety of important problems.

#####Linked Lists:

   - An array-based sequence is a collection of items where each item holds a **relative** position with respect to others

```python
scores = [85, 98, 50, 99, 76]
# how do we insert a number between scores?
```

   - Insertions and deletions at interior positions of an array-based sequence are expensive

   - Linked lists provide an alternative to an array-based sequence. Both array-based sequences and linked lists keep elements in a certain order, but using a very different style

   - If a `Node` is a 'tail' make sure the `next` of that `Node` is `None`

   - Insert by unlinking `next` for two pointers and creating a new `Node` with appropriate `next` value

   - just update pointers instead of modifying many, many `Nodes`

### Singly Linked List
###### The Good
   - linked list nodes can live anywhere in the memory.
   - as long as the references are updated, each linked list node can be flexibly moved to a different address
   - may change in size

###### The Bad
   - have linear look up time
   - when looking for a value in a linked list, you have to start from the beginning of the chain, and check one element at a time for a value you are looking for

#####Implementation:

```python 
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
      # notably, only has reference to the first/last element
      # no need to store entire contents of the list somehow
      # just need the start and end of the 'chain'

   def add(self, value):
      new_node = Node(value)
      new_node.next, self.head = self.head, new_node
      # adds to the top of the list
      # (new node becomes the head)
      # (old head becomes the 'next' for the newly added head)

```

#####Implementation of a Singly Linked List

   - `add(item)` adds a new item to beginning of the list

```python
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

```

   - `delete(item)` removes the item from the list
      + override `__delitem__`

```python
def __delitem__(self, value):
   # no items in list at all
   if self.isEmpty:
      return 'List is empty'

   # one item in list
   if len(self) == 1:
      self.head = None
      self.tail = None

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
```

   - `search(item)` finds an item in the list and returns boolean
      + override `__contains__` also

```python
def __contains__(self, value):
   current_node = self.head
   while current_node is not None:
      if current_node.value == value:
         return True
      current_node = current_node.next

   return False
```

   - `isEmpty` tests if list is empty, needs no params and returns bool
      + property

```python
@property
def isEmpty(self):
   # if list is empty then there is no head
   return self.head == None:

```

   - `size` returns number of items in the list
      + override `__len__` method as well

```python
def __len__(self):
   return self.length

def size(self):
   return self.length
```

   - `append(item)` adds a new item to the end of the list, returns nothing

```python
def append(self, e):
   new_node = Node(e)
   if self.isEmpty:
      self.head = new_node
      self.tail = new_node
      self.length += 1
      return
# of node is not empty
# set new node to be the next of whatever the current final node is
   self.tail.next = new_node
   self.tail = new_node
   self.length += 1
```

   - `insert(after, value)` adds new item after Node(after)

```python
# todo: insert(after, value)
```

   - `pop()` removes and returns the last item in the list

```python
# todo: pop()
```


##Stack

   - Collection of items where the addition of new items and removal of existing items always takes place at same end

####Basic Operations:

   + `push` adds element on top of stack
   + `pop` removes an element from the stack
   + `isEmpty` is `True` if stack is empty, otherwise `False`
   + `peek` returns the top element of the stack without removing it
   + `size` returns the number of items in the stack
   
   - Elements are inserted and removed according to the LIFO(Last in, First out), FILO(First in, Last out) principle

####Internally

   - when we have a push operation, we update pointer for the top
   - when we pop, we return the top and update the pointer for the top

   - say _s_ is a stack that has been created with no elements in it

```python
>>> s = Stack()
>>> pop()
"Error: stack is empty"
# or return None
None
>>> s.push(4)
# create a new node with value of 4
# new_node.next -> None
# point s.top at new_node
>>> s.push(5)
# create a new node pointing to None w value 5
# set new_node.next = top
# set top = new_node
>>> s.push(7)
# new_node(7)
# new_node.next = top
# top = new_node
>>> s.pop()
# popped = top
# top = top.next
# popped.next = None
# return popped
```

####Implementation using a List

```python
class Stack:
   def __init__(self):
      # todo: add from slides

```

####Implementation of New Data Structure Stack

```python
class Node:
   def __init__(self,value):
      self.value = value
      self.next = None

class Stack:
   def __init__(self):
      self.top = None
      self.length = 0

   @property
   def isEmpty(self):
      return self.top == None

```

####Infix and Postfix Expressions

- Infix expressions: mathematical expressions are written with the operator between the two operands (a + b)
- Postfix Expressions: operator follows the operands (a b +)

|Infix | PostFix|
|------|--------|
|4\*3+2\*1|4 3 2 1 \* + \*|

#####Implementation of postfix using stacks

`4 3 2 - 5 * +`

1. Scan until operator found (pushing numbers to the stack as you go along)
2. Pop two numbers when operator found
3. perform `3 - 2 = 1`
4. return `1` to stack
5. perform `1*5 = 5` and return `5` to stack
6. perform `5 + 4 = 9`
7. When finished there should be __exactly__ one _number_ in the stack

## Queue
- collection of items where the addition of new items happens at one end and the removal of existing items occurs at the other end

####Basic Operations
- `enqueue`: append to tail of queue
- `dequeue`: remove an element from head of queue
- `isEmpty`: returns `True` if queue is empty, otherwise `False`
- `peek`: returns element at head of queue without removing it
- `size`: returns number of items in the queue

- elements are inserted and removed according to the FIFO (First In, First Out) - LILO (Last In, Last Out) principle

```python
>>> q = Queue()
>>> q.dequeue()
"Error: queue is empty"
>>> q.enqueue(4)
# create new node with value 4
# head and tail both point to new_node
>>> q.enqueue(5)
# new_node = Node(5)
# tail.next = new_node
# tail = new_node
>>> q.enqueue(3)
# new_node = Node 3
# tail.next = new_node
# tail = new_node
>>> q.dequeue(4)
# temp = head
# head = head.next
# temp.next = None
# return temp
```

#### Implementation of Queue

###### As a List

```python
# todo: insert code from slides
```

###### As a New Data Structcure

```python
# todo: insert code from slides
```

#### Linear Data Structures
 - Design a method `reverse` in the LinkedList class that takes a linked list and changes the links between nodes to reverse the list

```python
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
```

 - A function takes a stack and returns a sorted stack (descending order from the top) What is the internal process if you are only allowed to use another temporary stack in such the function?

```python
# insert some code here maybe?
```

##Tree
   - Hierarchical data structure widely used with a root value and subtrees of children with a parent
   - tree is upside down, root on the top
   - tree consists of nodes and its connections are called edges
   - bottom nodeas also named leaf nodes / external nodes
   - Does not have a cycle, no loops in edges
   - Nodes with the same parent are called siblings

   - Subtree is a tree with a parent in a different tree
   - can go from root to every other node via edges

   - Important attributes
      + depth - number of levels from the top for a given node
      + level - all nodes on a given level have the same depth
      + height - number of levels
      + path

   - Types of Binary trees
      + full binary tree
         * Todo: Get definitions for Full and Complete
      + complete binary tree
      + perfect biary tree
         * every node has 2 children
      + degenerate binary tree
         * every node has 1 child

#####Properties of Binary Trees
   - a binary tree of n nodes has n-1 edges
   - for every k>= 1 there are no more than 2^k-1 nodes in level k
   - a binary tree with k levels has at most 2^k-1 leaves
   - the number of nodes on the last level is at most the sum of the number of nodes on all other levels plus 1
   - a binary tree with k levels has no more than 2^k -1 nodes


####Binary Search Tree
 - A tree in which all the nodes follow the following properties
    + The left subtree of a node has a key less than or equal to its parent node's tree
    + The right subtree of a node has a key greater than its parent node's key
    + The left and right subtree are also binary search trees

######Implementation of a Binary Search Tree

```python

class binarySearchTree:
   def __init__(self):
      self.root = None

   def insert(self, node, value):
      if node == None:
         self.root = Node(value)
      else:
         if value < node.value:
            if node.left == None:
               node.left = Node(value)

            else:
               self.insert(node.left, value)
         else:
            if(node.right == None):
               node.right = Node(value)
            else:
               self.insert(node.right, value)

```

### Traversal of Binary Trees
- refers to the process of visiting all the nodes in the tree
- since a binary tree has no cycles, we start the traversal from the root node
- because the tree is hierarchical, there is no unique traversal

#####Breadth-First Search (BFS)
- traverses the tree in level order: visits every node on a level before going to a lower level

Todo: Find pictures for the trees, #steal from the lecture slides

#####Depth-First Search (DFS)
- go as deep as possible down one path before backing up and trying a different one
- 3 Commonly used DFS traversals to visit all the nodes in a tree. They differ by the order in which each node is visited
      + Preorder Traversal (Root -> Left -> Right)
      + Inorder Traversal (Left -> Root -> Right)
      + Postorder Traversal (Left -> Right -> Root)


#### Application in Calculator
3+(4*5 + (2-3))

- leafs are all numbers
- roots are operators
- one operator for 2 numbers
- inorder will give same expression
- postorder will give the postfix expression
      + can be easily calculated using a stack
      + 3 4 5 * 2 3 - + +
- preorder gives prefix expression
      * + 3 5 etc you know

###Implementation of Binary Search Tree
- Includes other traversal methods

######Queue Class For Traversals
```python
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

```

######Binary Search Tree Class w/ Node
```python
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
```

###### Breadth First Search
```python
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
```

######Recursive Preorder

```python
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
```

######Recursive Inorder

```python
def inorder(self, node):
   # similar to preorder (just different order)
   if node is not None:
      # inorder = left root right
      self.inorder(node.left)
      print(node.value, end = ' ')
      self.inorder(node.right)
```

######Recursive Postorder

```python
def postorder(self, node):
   if node is not None:
      # postorder = left right root
      self.inorder(node.left)
      self.inorder(node.right)
      print(node.value, end = ' ')
```

######Legible Representation using `__str__` and `__repr__`

```python
# todo: Implement legible representation overriding __repr__
```

##Graphs

   - A data structure with nodes (also called vertices) that are connected by edges
   - Graphs can be undirected or directed
      * directed = one way to travel along edges
      * undirected = can travel both ways along the edges
   - Edges can represent distance or weight or whatever
      * Edges can have values
      * Values called 'costs'
         + A travels to B with cost 5
   - Graphs can contain cycles
      + Cyclic = undirected with cycle
      + Acyclic graph = undirected with no cycle
      + Acyclic can also be directed with a cycle, but cannot travel along it
      + Cyclic can be directed graph with travelable cycle
   
####Key Terms
   - **Vertex**: a fundamental part of a graph, can have name and additional information
   - **Edge**: connects two vertices to show a relationship between them, can be one-way or two-way
   - **Weight**: Edges may be weighted to show that there is a cost to go from one vertex to another
   - **Path**: sequence of vertices that are connected by edges
   - **Cycle**: a cycle in a directed graph is a path that starts and ends at the same vertex, a graph with no cycles is acyclic, a directed graph with no cycles is a Directed Acyclic Graph (DAG)


   - A graph can be represented as `G=(V,E)`, where V is a set of vertices and E is a set of Edges. Each edge is a tuple `(v,w)` where `w`, `v` are Vertices

####Edges
   - **Tree edge**: edges that we encounter while down one path of a graph
   - **Non-Tree Edge**:
      + **Forward Edge**: allows us to move forward through the graph, and could potentially be part of another paht down the tree
      + **Backward Edge**: connects a node in a graph back up to one of its ancestors or itself
      + **Cross Edge**: connects to sibling nodes that don't necessarily share an ancestor in a tree path, but connects them anyways

   - In an undirected graph, there are no forward edges or cross edges. Every single edge must be either a tree edge or a backward edge 

####Connections

######Strongly connected
   - A graph is strongly connected if for every vertex there is some path from u to v and from v to u

   - G = (V, E) where:
      + V={A,B,C,D,E}
      + E={(A,C,12),AD60,BA10,CB20,CD32,EA7}
      + Path from A to B = (A, C, B)
      + Cycle = ...


###Graph Implementation
##### Adjacency Matrix
   + when two vertices are connected by an edge, we say they are adjacent
   + rows and columns labeled with nodes
   + (Strictly speaking, rows are where edge originates, columns are where edge is directed)
   + table populated with weights (1 for undirected/unweighted)

|     |A|B|C|D|E|F|
|-----|-|-|-|-|-|-|
|**A**| |1|1| | | |
|**B**|1| |1|1| |1|
|**C**|1|1| | |1| |
|**D**| |1| | | | | 
|**E**| | |1| | | | 
|**F**| |1| | | | |


- Most of it is empty, use something else that takes up less space

##### Adjacency List
- Use dict where keys are the vertices and values are all the other nodes it is connected to
```
A: B,C
B: A,C,D,F
C: A,B,E
D: B
E: C
F: B
```

####Graph Traversals
- Breadth first search: starts at an arbitrary nde in a graph and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level
      * Use queue data structure to help
- Depth first search:  It starts at some arbitrary node in a graph and explores as far as possible along each branch before backtracking
      * Use stack data structure to help

*Choose alphabetical/numerical order nodes first (no left/right)*

####Dijkstra's Algorithm
- From starting node, visit node with smallst known distance
- once you have moved to the smallest-distance node, check each neighboring node
- for each neighboring node, compute the distance for the neighboring nodes by summing the distance of the edges leading from the start node
- if the distance to a node is less than a known distance, update the shortest distance for that node

1. store visited and unvisited nodes
2. Choose A to start
      1. visit adjacent nodes to A
      2. add the cost of edge between start and new adjacent nodes
      3. Replace shortest distance (inf) with new shortest distance from A
      4. Put A in previous node section, visited

3. Choose C (shortest known distance)
      1. visit adjacent nodes to C
      2. add cost of edge to new adjacent node from C + previous cost for C
      3. ...

4. Choose B (shortest known distance not yet visited)
      1. ignore distance to A (already visited)
      2. check adjacent node distances...
      3. repeat
5. repeat until all nodes are in visited list

- Can rebuild path by going backwards from target to start, looking at 'Previous Node'


##Hash Tables
- Collection of items which are stored in such a way as to make them easy to find later
- Each position of the hash table, often called a `bucket`, can hold an item and is named by an integer value starting at 0
- Basically Math Parkour, get from one place to another with the strangest and most creative math you can think of

###Hash Function
- The mapping between an item and the bucket where that item belongs in the hash table is the Hash Function
- must be efficiently computable and should uniformly distribute the keys
- modular method is the most common hash function, just takes an item and divides it by the table size, returning the remainder as its hash value
- Important aspect of hash functions: Non-reversible (easily)

###Modular Hashing
- once the hash values have been computed we can insert each item into the hash table at the designated position
- The load factor (\lambda) of a hash table is commonly denoted by (\lambda) = (#of items) / (table size)
- Load Factor basically = What percent of the table is full

###Collision
- when we want to search for an item, use hash function to compute the bucket name for the item and check table to see if it is present
- Only works if each item maps to a unique location in the hash table
- collision when two or more items need to be in the same bucket, and it creates problems for the hashing technique
- Probability of a collision increases as load factor -> 1 (actually even .5)

####Perfection
- A hash function that maps each item into a unique bucket is a Perfect Hash Function
- Unfortunately, given an arbitrary collection of items, there is no systematic way to construct a perfect hash function.
- the goal is to create a hash function that minimizes the number of collisions, is easy to compute, and evenly distributes the items in the hash table
- Simple but Secure

####Folding Method
- divide the item into equal size pieces (the last piece may not be of equal size)
      + 814 865-4701
- add the pieces to obtain the item to be hashed
      + 81 + 48 + 65 + 47 + 01 = 242
- some folding methods go one step further and reverse every other piece 
before the addition
      + 81 + 84 + 65 + 74 + 01 = 305

- for hash table of size 12:
      * 242%12 = 2
      * 305%12 = 5

####Mid-Square Method
- Square the item
- Extract some portion of the resulting digits
      * 65^2 = 4225 => Choose 22, 42, 45, whatever you want just be consistent
- Hash em up

####Hashing Strings
- convert each haracter of the string into ordinal values
- add ordinal values and use modular method to get a hash value

###Collision Resolution
- Extremely important to be consistent when this happens

####Open Addressing
- Try to find the next open bucket in the hash table
- in General:
      * Get from slides

- visiting each bucket one at a time is an open addressing type called Linear Probing
- What happens when we want to go backwards
      * 20%11 = 9 -> look in 9
      * Cant say 20 is not in the hash table if it isnt in 9
      * couldve been a collision
      * Because we used linear probing, we have to look through the next buckets until we either have a 20, or we have an empty bucket

#####Clustering
- when many collisions occur at the same hash value, a number of surrounding buckets will be filled by the linear probing resolution
- A big cluster of buckets around the 'problem bucket' will be occupied, this becomes an issue bc then the rest of the buckets near there are filled and the hash table is not filled efficiently


- Resolution
      - dont put the collided item in the next open probe, look +3 or +4 ...
      - This ensures that the items that cause collisions would be more evenly distributed in the hash table

- TODO: Get notes from the slides for this entire section

- Chaining
      * allows each bucket to hold a reference to a collection of items
      * chaining allows many items to exist at the same place in the hash table
      * when collisions happen, the item is stll placed in the proper bucket of the hash table
      * as more items hash to the same location, the difficulty of searching for the item in the collection increases
         - use a nested hash table? can we do this?
         - I think so.

- Remember 
      + if the load factor is small, then there is a lower cahnce of collisions, meaning that the items are more likely to be in the buckets where they belong
      + If the load factor is large, meaning that the table is filling up, then there are more and more collisions, this means that collision resolution is more difficult, requiring more comparisions to find an empty bucket
      * usually have quite a bit more buckets than items 

--------------------------------
#Searching and Sorting Algorithms

- Searching is the algorithmic process of finding a particular item in a collection of items
- A search typically answers `True` or `False` as to whether the item is present and sometimes it may be modified to return where the item is found
- sorting is the process of placing elements from a collection in some kind of order
- sorting a large number of items can take a substantial amount of computing resources
- the efficiency of searching and sorting algorithms is related to the number of items being processed


##Searching

- Need to look at every single item in the list to make sure that the item is / is not in the list
      * *if the list is unsorted*

####Binary Search
- takes a sorted list and starts by examining the middle item, the ordered nature of the list allows us to eliminate half of the items
- to find the item x in a list with n elements using binary search:
      1. Compare x with the middle element
      2. If x matches the middle element, return true
      3. If x is greater than the middle element then x can only be in right half of subarray after the middle element. So we recur for right half
      4. If x is smaller, recur for the left half.

#####Divide-and-Conquer Paradigm
- A problem that we want to solve may be too big to understand or solve at once
- TODO: Go back and get these notes, quick sort, merge sort, insertion sort etc.


-------
#Analysis of Algorithms
How good are we at doing computers? How do we know?

   - We have to be concerned about the resources consumed by the program
      + Time
      + Memory
   - These are totally different resources
   - We could choose a program with limited memory that runs slowly, or one that takes loads of memory and finishes quickly
   - Algorithm analysis does not answer the question of how much of a resource is consumed to process n pieces of data
      - it cares more about the growth rate of the resource consumption with respect to the data size
         - **Worst Case** - max number of steps taken on any instance of size n
         - **Best Case** - minimum umber of steps taken on any instance of size n
         - **Average Case** - an average number of steps taken on any instance of size n 


