#Lab #7
#Due Date: 10/05/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this program by myself, 
#    using only the class materials             
#  
########################################


#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)
###################


def recursive_triangle(k, n):
    '''
        Takes two integers k and n
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    # --- YOUR CODE STARTS HERE
    # base case if the number of remaining rows in the triangle is 1
    if k == 1:
      # print the whitespace corresponding to number of spaces n-k and then *
      return ' '*(n-k) + "*"
    # otherwise return n-k spaces and then k *'s
    # + the rest of the triangle with k-1 remaining rows
    return ' '*(n-k) + '*'*k +'\n' + recursive_triangle(k-1, n)
    # --- YOUR CODE ENDS HERE
