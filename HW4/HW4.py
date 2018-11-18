#HW 4
#Due Date: 11/16/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program by myself 
#                          using only the class materials       
#
########################################

#Name: James Blaszkiewicz

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

# ----    Copy your Stack (or Queue) code from LAB9 (or LAB10) here ---------                         

class Stack:
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

# ----    Stack (or Queue) code ends here here ---------

def findNextOpr(txt):
    #--- Copy your function code from HW3 here ----#
    if len(txt)<=0 or not isinstance(txt,str):
        return "type error: findNextOpr"
    
    # set mindex to length of txt because no valid index will be greater than that 
    mindex = len(txt)
    operators = ['+', '-', '*', '/', '^']
    for i in range(len(operators)):
        nextOper = txt.find(operators[i])

        # if the operator is not in the text, continue. sending it to the elif
        # would result in a -1 mindex which would be wrong
        if nextOper == -1:
            continue
        elif nextOper < mindex:
            mindex = nextOper

    # if no operators found, ret -1, otherwise ret mindex
    return -1 if mindex == len(txt) else mindex
    
    #--- function code ends -----#


def isNumber(txt):
    #--- Copy your function code from HW3 here ----#
    if not isinstance(txt, str):
        return "type error: isNumber"
    if len(txt)==0:
        return False

    # try casting txt to float
    try:
        float(txt)
        return True
    # if it doesn't work, txt might be a negative with a space (- 4)
    except:
        # check if there is a negative sign
        if txt.find('-') != -1:
            return True
        return False
    #--- function code ends -----#


def getNextNumber(expr, pos):
    #--- Copy your function code from HW3 here ----#
    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        return None, None, "type error: getNextNumber"

    # set remaining txt variable
    remaining = expr[pos:]
    # initialize to None so that if they are not changed, they return correctly
    nextOpr = None
    nextOprPos = None
    
    # if there is a negative number
    if remaining.strip()[0] == '-':
        negate = 1 + remaining.find('-')
        if findNextOpr(remaining[negate:]) != -1:
            nextOprPos = negate + findNextOpr(remaining[negate:])
            nextOpr = remaining[nextOprPos]
    else:
        # if it found an operator, set it to nextOprPos, set actual character to nextOpr
        if findNextOpr(remaining) != -1:
            nextOprPos = findNextOpr(remaining)
            nextOpr = remaining[nextOprPos]
    
    nextNum = None

    # this entire mechanism breaks if there are any spaces, so no spaces.
    if isNumber(remaining[:nextOprPos]):
        nextNum = float(remaining[:nextOprPos].replace(" ", ""))

    # add position back on to nextOprPos
    if nextOprPos != None:
        nextOprPos += pos

    return (nextNum, nextOpr, nextOprPos)
    #--- function code ends -----#
    

def exeOpr(num1, opr, num2):
    #This funtion is just an utility function. It is skipping type check
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        if num2==0:
            print("Zero division error")
            return "error"
        else:
            return num1/num2
    elif opr=="^":
        return num1 ** num2
    else:
        print("error in exeOpr")
        return "error"


def matchingParen(expr):
    openParens = Stack()
    closedParens = Stack()
    for i in expr:
        if i == '(':
            openParens.push(i)
        elif i == ')':
            closedParens.push(i)

    return len(openParens) == len(closedParens)

    
def _calculator(expr):
    #--- Copy the body of your calculator(expr) function from HW3 here ----#

    if len(expr)<=0 or not isinstance(expr,str): #Line A     
        return "input error line A: calculator"
    
    # Concatenate '0' at the beginning of the expression if it starts with a negative number to get '-' when calling getNextNumber
    # "-2.0 + 3 * 4.0 ” becomes "0-2.0 + 3 * 4.0 ”. 
    expr=expr.strip()
    if expr[0]=="-":
        expr = "0 " + expr
    newNumber, newOpr, oprPos = getNextNumber(expr, 0)   

    # Initialization. Holding two modes for operator precedence: "addition" and "multiplication"
    if newNumber is None: #Line B
        return "input error line B: calculator"
    elif newOpr is None:
        return newNumber
    elif newOpr=="+" or newOpr=="-":
        mode="add"
        addResult=newNumber     #value so far in the addition mode   
        mulLastOpr=None  # no multiplication so far
        mulResult=0
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber     #value so far in the mulplication mode
        addLastOpr = "+"
        mulLastOpr = newOpr
    elif newOpr=='^':
        mode='exp'
        addResult=0
        mulResult=0
        addLastOpr = '+'
        mulLastOpr=None
        base = newNumber # store base of exponentiation
    pos=oprPos+1                #the new current position
    opr=newOpr                  #the new current operator
    
    #Calculation starts here, get next number-operator and perform case analysis. Compute values using exeOpr 
    while True:
        # --- YOU CODE STARTS HERE
        # get newNumber, newOpr, oprPos
        newNumber, newOpr, oprPos = getNextNumber(expr, pos)
        
        # handle if final character (w/o spaces) is an operator
        if expr.strip()[-1] in '+-/*^':
            return 'error: line ends in operator'
        
        # catch error two numbers with no operator from getNextNumber sentinel
        elif oprPos == -1:
            return 'error: no operator between numbers'

        elif newNumber is None:
            return 'error: no number between operators'

        elif mode == 'add':
            # dont need to store previous */ anymore bc everything stored in addRes
            # when mode is changed to add
            mulLastOpr = None

            if newOpr == None:
                # finish calculation in add mode
                return exeOpr(addResult, opr, newNumber)
            elif newOpr == '+' or newOpr == '-':
                # if we still have operators, finish previous calculation
                addResult = exeOpr(addResult, opr, newNumber)
            elif newOpr == '*' or newOpr == '/':
                # changing modes to multiplication
                mode = 'mul'
                # mul result = new num because if we're already in add mode, 
                # any previous mulResult should have been stored in addResult
                mulResult = newNumber
                # store previous operator to addLastOpr for if we switch back again
                addLastOpr = opr
            elif newOpr == '^':
                # changing mode to exponentiation
                mode = 'exp'
                addLastOpr = opr
                base = newNumber

        elif mode == 'mul':            
            
            if newOpr is None:
                # finish addition bc no more operators
                mulResult = exeOpr(mulResult, opr, newNumber)
                return exeOpr(addResult, addLastOpr, mulResult)
            # if mode does not change
            elif newOpr == '*' or newOpr == '/':
                mulResult = exeOpr(mulResult, opr, newNumber)

            # if mode changes back to add
            elif newOpr == '+' or newOpr == '-':
                mulResult = exeOpr(mulResult, opr, newNumber)
                # set mode to add
                mode = 'add'
                # update addResult with its add/sub to mulResult
                mulLastOpr = opr
                # store mulLastOpr in case of exponentiation
                addResult = exeOpr(addResult, addLastOpr, mulResult)

            elif newOpr == '^':
                mode = 'exp'
                mulLastOpr = opr
                base = newNumber

        elif mode == 'exp':
            expResult = exeOpr(base, opr, newNumber)

            if newOpr is None:
                # if we multiplied and did not add after:
                if mulLastOpr is not None:
                    expResult = exeOpr(mulResult, mulLastOpr, expResult)
                # return finished addition with finished multiplication
                return exeOpr(addResult, addLastOpr, expResult)

            elif newOpr == '+' or newOpr == '-':
                mode = 'add' 
                
                # if we multiplied without adding after right before entering
                # exponentiation
                if mulLastOpr is not None:
                    expResult = exeOpr(mulResult, mulLastOpr, expResult)

                addResult = exeOpr(addResult, addLastOpr, expResult)

            elif newOpr == '*' or newOpr == '/':
                mode = 'mul'

                # if we multiplied right before entering exponentiation
                if mulLastOpr is not None:
                    mulResult = exeOpr(mulResult, mulLastOpr, expResult)

                else:
                    # otherwise store expResult alone in mulResult
                    mulResult = expResult
                    # if we did not have this if/else, we would always multiply by zero
                    # before switching to multiplication
                    # ie 2^3 * 2 would result as 0 instead of 16



        # update pos and opr with current values

        pos = oprPos+1
        opr = newOpr
    #--- function code ends -----#


def calculator(expr):
    # Required: calculator must create and use a Stack (or Queue) for parenthesis matching
    # Call _calculator to compute the inside parentheses
    if not isinstance(expr,str) or len(expr)<=0: 
        return "input error in calculator"
    # expr = expr.replace(" ", "")
    expr = expr.strip()
    # check for equal number of open and closed parens
    if not matchingParen(expr):
        return 'error: mismatched parentheses'
    s = Stack()        # You must use the Stack s

    #Scan the expression to find the most inner expression, note that if pos==-1 you can try to compute the expression as is
    pos = expr.find("(")
    while True:
    #--- function code starts here -----#
        
        # scan expression for open parenthesis
        while pos != -1:
            # push next open paren to stack
            s.push(pos)

            # if there are no more open parens, set nextOpen to -1
            if expr[pos+1:].find('(') == -1:
                nextOpen = -1
            # otherwise set nextOpen to the position in expr of the next open paren
            # need to add pos+1 back to expr because it was sliced before the find()
            else:
                nextOpen = pos+1 + expr[pos+1:].find('(')

            # find next closed paren
            nextClosed = expr.find(')')
            
            # if the next closed paren comes before the next open paren (i.e. we have a completed set of () )
            # or there are no more open parens
            if nextClosed < nextOpen or nextOpen == -1:
                # get pos of last open paren from stack
                open_paren = s.pop()
                # calculate inner paren result
                result = _calculator(expr[open_paren+1:nextClosed])

                # if the expression was written using paren as multiply (i.e. 2(4+1) ) add a '*' before adding result
                if isNumber(expr[open_paren-1]) and open_paren != 0:
                    expr = expr[:open_paren]  + str(result) + expr[nextClosed+1:]

                # otherwise rebuild expr normally
                else:
                    expr = expr[:open_paren] + str(result) + expr[nextClosed+1:]

                # need to use find again on expr because we rebuilt expr
                pos = expr.find('(')

            # otherwise (we did not rebuild expr) set pos to nextOpen which was found earlier
            else:
                pos = nextOpen

        # if there are too many ')' then there will still be some left, raise error
        if expr.find(')') != -1:
            return 'error: mismatched parentheses'
        # otherwise return result of _calc on whole expression
        return _calculator(expr)
            
    #--- function code ends here-----#