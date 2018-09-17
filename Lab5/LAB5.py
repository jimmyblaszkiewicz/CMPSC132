#Lab #5
#Due Date: 09/21/2018, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
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

    #-- ends here ---

    def purchase(self):
    #-- start code here ---

    #-- ends here ---

    def deposit(self, amount):
    #-- start code here ---

    #-- ends here ---

    def restock(self, amount):
    #-- start code here ---

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

    #-- ends here ---
    
    #PROPERTY METHODS

    def distance(self):
    #-- start code here ---

    #-- ends here ---
       
    def slope(self):
    #-- start code here ---

    #-- ends here ---
            
