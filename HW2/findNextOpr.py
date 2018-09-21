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
    operators = ['+', '-', '/', '*']
    mindex = len(txt)
    for i in range(len(operators)-1):
        nextOper = txt.find(operators[i])
        if nextOper == -1:
            continue
        elif nextOper < mindex:
            mindex = nextOper

    return -1 if mindex == len(txt) else mindex

    # ---  CODE ENDS HERE