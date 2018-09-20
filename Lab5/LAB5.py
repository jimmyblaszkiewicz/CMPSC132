#Lab #5
#Due Date: 09/21/2018, 11:59PM
########################################
#                                      
# Name: James Blaszkiewicz
# Collaboration Statement: I worked on this lab by myself using 
# only the class materials.             
#
########################################


class SodaMachine:
    '''
        Creates instances of the class SodaMachine. Takes a string and an integer

        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    #-- start code here ---
    # initialize attributes if they are correct type
        if type(product) == str and type(price) == int:
            self.product = product
            self.price = price
            self.Balance = 0
            self.stock = 0
        else:
            return('Invalid input')
    #-- ends here ---

    def purchase(self):
    #-- start code here ---
        # if you can purchase the product
        if self.stock > 0 and self.Balance >= self.price:
            self.stock -= 1
            # if balance is the same as price, dont print 'take your ...'
            if self.Balance == self.price:
                self.Balance -= self.price
                return '{} dispensed'.format(self.product)

            # if there is leftover balance, print 'take your ...'
            elif self.Balance > self.price:
                # sets a leftover variable for the message
                # sets balance to 0 b/c 'given' back to the user
                self.leftover = self.Balance - self.price
                self.Balance = 0
                return '{} dispensed, take your ${}'.format(self.product, self.leftover)

        
        # not enough product
        elif self.stock == 0:
            return 'Product out of stock'
        
        # not enough balance
        elif self.Balance < self.price:
            return 'Please deposit ${}'.format(self.price-self.Balance)

        #-- ends here ---

    def deposit(self, amount):
    #-- start code here ---
        # if stock is more than 0, deposit amount into Balance
        if self.stock > 0:
            self.Balance += amount
            return 'Balance = ${}'.format(self.Balance)

        # otherwise, do not set Balance, send message to user indicating
        # lack of stock
        else:
            return 'Sorry, out of stock. Take your ${} back'.format(amount)
    #-- ends here ---

    def restock(self, amount):
    #-- start code here ---
        # adds amount to stock
        self.stock += amount
        return 'Current soda stock: {}'.format(self.stock)
    #-- ends here ---
    

class Line:
    ''' 
       Creates objects of the class Line, takes 2 tuples
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''

    
    def __init__(self, coord1, coord2):
    #-- start code here ---
        # make sure both coords given are tuples
        # and that they have the same number of components
        if type(coord1) == tuple and type(coord2) == tuple and len(coord1) == len(coord2):
            self.coord1 = coord1
            self.coord2 = coord2
            

        else:
            print("Invalid input")

    #-- ends here ---
    
    #PROPERTY METHODS
    @property
    def distance(self):
    #-- start code here ---
         # distance formula btw a,b and x,y is
         # sqrt((a-x)^2 + (b-y)^2)

        # need sqrt() from math module
        import math

        # create list of squares of differences btw x y components
        self.squares = []
        for i in range(len(self.coord1)):
            self.squares.append((self.coord1[i] - self.coord2[i])**2)

        # return sqrt of sum of squares rounded to 3 decimal places
        return(round(math.sqrt(sum(self.squares)), 3))

    #-- ends here ---

    @property
    def slope(self):
    #-- start code here ---
        # slope between two coords is the rise / run
        # so btw a,b and x,y it is
        # (y-b)/(x-a)

        # if x values are equal then slope is infinity
        if self.coord1[0] == self.coord2[0]:
            return 'Infinity'

        # rounded y1-y2/x1-x2 to 3 decimal places
        return(round((self.coord2[1]-self.coord1[1])/(self.coord2[0] - self.coord1[0]), 3))


    #-- ends here ---

