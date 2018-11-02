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



# ----    Stack (or Queue) code ends here here ---------




def findNextOpr(txt):
    #--- Copy your function code from HW3 here ----#

    #--- function code ends -----#


def isNumber(txt):
    #--- Copy your function code from HW3 here ----#

    #--- function code ends -----#

def getNextNumber(expr, pos):
    #--- Copy your function code from HW3 here ----#

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

    
def _calculator(expr):
    #--- Copy the body of your calculator(expr) function from HW3 here ----#

    #--- function code ends -----#

def calculator(expr):
    # Required: calculator must create and use a Stack (or Queue) for parenthesis matching
    # Call _calculator to compute the inside parentheses
    if not isinstance(expr,str) or len(expr)<=0: 
        return "input error in calculator"
    expr = expr.strip()
    s = Stack()        # You must use the Stack s
    ##OR
    #q = Queue()

    #Scan the expression to find the most inner expression, note that if pos==-1 you can try to compute the expression as is
    pos = expr.find("(")
    while True:
    #--- function code starts here -----#


    #--- function code ends here-----#