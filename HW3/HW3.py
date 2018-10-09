#HW 3
#Due Date: 10/20/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this HW by myself using only the 
# class materials.             
#
########################################


def findNextOpr(txt):
    """
        Takes a string and returns -1 if there is no operator in txt, otherwise returns 
        the position of the leftmost operator. +, -, *, / are all the 4 operators

        >>> findNextOpr('  3*   4 - 5')
        3
        >>> findNextOpr('8   4 - 5')
        6
        >>> findNextOpr('89 4 5')
        -1
    """
    if len(txt)<=0 or not isinstance(txt,str):
        return "type error: findNextOpr"

    # --- YOU CODE STARTS HERE
    
    # set mindex to length of txt because no valid index will be greater than that 
    mindex = len(txt)
    operators = ['+', '-', '*', '/']
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
    
    # ---  CODE ENDS HERE

def isNumber(txt):
    """
        Takes a string and returns True if txt is convertible to float, False otherwise 

        >>> isNumber('1   2 3')
        False
        >>> isNumber('-  156.3')
        False
        >>> isNumber('29.99999999')
        True
        >>> isNumber('    5.9999 ')
        True
    """
    if not isinstance(txt, str):
        return "type error: isNumber"
    if len(txt)==0:
        return False

    # --- YOU CODE STARTS HERE
    # try casting txt to float
    try:
        float(txt)
        return True

    # if it doesn't work, txt is not a number
    except:
        return False

    # ---  CODE ENDS HERE

def getNextNumber(expr, pos):
    """
        expr is a given arithmetic formula of type string
        pos is the start position in expr
          1st returned value = the next number (None if N/A)
          2nd returned value = the next operator (None if N/A)
          3rd retruned value = the next operator position (None if N/A)

        >>> getNextNumber('8  +    5    -2',0)
        (8.0, '+', 3)
        >>> getNextNumber('8  +    5    -2',4)
        (5.0, '-', 13)
        >>> getNextNumber('4.5 + 3.15         /   5',0)
        (4.5, '+', 4)
        >>> getNextNumber('4.5 + 3.15         /   5',10)
        (None, '/', 19)
    """

    if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
        return None, None, "type error: getNextNumber"
    # --- YOU CODE STARTS HERE

    # set remaining txt variable
    remaining = expr[pos:]
    # initialize to None so that if they are not changed, they return correctly
    nextOpr = None
    nextOprPos = None
    
    # if it found an operator, set it to nextOprPos, set actual character to nextOpr

    if findNextOpr(remaining) != -1:
        nextOprPos = findNextOpr(remaining)
        nextOpr = remaining[nextOprPos]

    
    # find next number before the next operator
    # strip into noSpaces to feed into isNumber
    noSpaces = remaining[:nextOprPos].split()
    nextNum = None

    # walk through noSpaces to find first item that passes isNumber()
    for i in noSpaces:
        if isNumber(i):
            nextNum = float(i)


    # add position back on to nextOprPos
    if nextOprPos != None:
        nextOprPos += pos

    # if there is more than 1 number in front of the next operator
    # set nextOprPos = -1 so calculator() can catch error
    if len(noSpaces) > 1:
        nextOprPos = -1

    return (nextNum, nextOpr, nextOprPos)
    



    # ---  CODE ENDS HERE

def exeOpr(num1, opr, num2):

    #This function is just an utility function for calculator(expr). It is skipping type check

    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        if num2 != 0:
            return num1/num2
        else:
            return 'error: divide by zero'
    elif opr=="^":
        return num1**num2
    else:
        return "error in exeOpr"
    
def calculator(expr):
    """
        Takes a string and returns the calculated result if the arithmethic expression is value,
        and error message otherwise 

        >>> calculator("   -4 +3 -2")
        -3.0
        >>> calculator("-4 +3 -2 / 2")
        -2.0
        >>> calculator("-4 +3   - 8 / 2")
        -5.0
        >>> calculator("   -4 +    3   - 8 / 2")
        -5.0
        >>> calculator("23 / 12 - 223 + 5.25 * 4 * 3423")
        71661.91666666667
        >>> calculator("2 - 3*4")
        -10.0
        >>> calculator("4++ 3 +2")
        'error message'
        >>> calculator("4 3 +2")
        'input error line B: calculator'
        
        Homework 3: Now with Exponents (not nested though)
        >>> calculator(“-5 + 60 / 3^3 * 4 - 2 * 4^2”)
        -28.11111111111111
        >>> calculator("4^2 / 2^2")
        4.0
        >>> calculator("-4^ / 2^2")
        'error: no number between operators'
    """


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
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        mulResult=newNumber     #value so far in the mulplication mode
        addLastOpr = "+"
    pos=oprPos+1                #the new current position
    opr=newOpr                  #the new current operator
    
    #Calculation starts here, get next number-operator and perform case analysis. Compute values using exeOpr 
    while True:
        # --- YOU CODE STARTS HERE
        # get newNumber, newOpr, oprPos
        newNumber, newOpr, oprPos = getNextNumber(expr, pos)
        
        # handle if final character (w/o spaces) is an operator
        if expr.strip()[-1] in '+-/*':
            return 'error: line ends in operator'
        
        # catch error two numbers with no operator from getNextNumber sentinel
        elif oprPos == -1:
            return 'error: no operator between numbers'

        elif newNumber is None:
            return 'error: no number between operators'

        elif mode == 'add':
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

        elif mode == 'mul':
            # just multiply right away, dont need to save anything except in mulResult
            mulResult = exeOpr(mulResult, opr, newNumber)
            
            if newOpr is None:
                # finish addition bc no more operators
                return exeOpr(addResult, addLastOpr, mulResult)

            # if mode changes back to add
            elif newOpr == '+' or newOpr == '-':
                # set mode to add
                mode = 'add'
                # update addResult with its add/sub to mulResult
                addResult = exeOpr(addResult, addLastOpr, mulResult)


        # update pos and opr with current values

        pos = oprPos+1
        opr = newOpr
        







    # ---  CODE ENDS HERE