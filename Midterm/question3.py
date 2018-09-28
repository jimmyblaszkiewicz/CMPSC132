'''
James Blaszkiewicz
CMPSC 132 Midterm
Question 3

Create a Complex class that performs operations on complex numbers
by overriding the __add__, __sub__, and __mul__ methods
'''

class Complex:

    def __init__(self, alpha, beta):
        # initialize attributes
        self.alpha = alpha
        self.beta = beta

    def __str__(self):
        return "({}, {}i)".format(self.alpha, self.beta)

    def __repr__(self):
        # format alpha and beta with i
        return "({}, {}i)".format(self.alpha, self.beta)


    def __add__(self, other):
        # simply add alpha1 to alpha2 and beta1 to beta2
        newAlpha = self.alpha + other.alpha
        newBeta = self.beta + other.beta

        # in general each of these operations will return a new instance Complex 
        # instead of altering either involved in the operation
        return Complex(newAlpha, newBeta)

    def __sub__(self, other):
        # simply sub alpha2 from alpha1 and beta2 from beta1
        newAlpha = self.alpha - other.alpha
        newBeta = self.beta - other.beta

        return Complex(newAlpha, newBeta)

    def __mul__(self, other):
        # general rule for multiplication of complex numbers
        newAlpha = (self.alpha * other.alpha) - (self.beta * other.beta)
        newBeta = (self.alpha * other.beta) + (self.beta * other.alpha)

        return Complex(newAlpha, newBeta)