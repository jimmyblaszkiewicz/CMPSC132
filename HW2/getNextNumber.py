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

    # list of operators and minimum index variable initialization
    operators = ['+', '-', '/', '*']

    # set mindex to length of txt because no valid index will be greater than that 
    mindex = len(txt)

    for i in range(len(operators)-1):
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
    except ValueError as e:
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
    # split into pieces to feed into isNumber
    pieces = remaining[:nextOprPos].split()
    nextNum = None
    # walk through pieces to find first item that passes isNumber()
    for i in pieces:
        if isNumber(i):
            nextNum = float(i)

    # add position back on to nextOprPos
    if nextOprPos != None:
        nextOprPos += pos

    return nextNum, nextOpr, nextOprPos
    # ---  CODE ENDS HERE