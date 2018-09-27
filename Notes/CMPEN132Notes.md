

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

### Pros and Cons
#### Pros
   - make the code look clean and elegant
   - complex task can be broken down into simpler subproblems using recusion
   - sequence generation is easier with recursion than using nested iteration

#### Cons
   - logic is hard to follow
   - expensive bc takes up lots of memory and time
   - hard to debug
