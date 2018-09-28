'''
James Blaszkiewicz
CMPSC 132 Midterm
Question 4

Create a recursive function(x, n) to calculate x^n, recursively
'''

def power(base, exp):
    # x^n = x * x^(n-1)
    # x^(n-1) = x * x^((n-1)-1) ... 
    # if n == 0, return 1

    if exp == 0:
        return 1

    return base * power(base, exp-1)