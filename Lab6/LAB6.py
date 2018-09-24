#Lab #6
#Due Date: 09/30/2018, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################

class Vector:
    '''
        Takes a list and creates a Vector object to perform vector operations
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([7,8,9])
        >>> x+y
        Vector([9, 12, 15])
        >>> x-y
        Vector([-5, -4, -3])
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        100
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''
    def __init__(self, vector):
        self.vector = vector

    #To compare and determine if both Vector objects are equal
    #Include this in your final submission
    def __eq__(self, other):
        return self.vector==other.vector

    # --- Your code starts here
       
    # --- ends here