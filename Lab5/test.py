import unittest 
from LAB5 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for SodaMachine Class
    def test_not_enough_stock(self):
        # tests if there is not enough stock for a purchase
        m = SodaMachine('Coke', 10)
        self.assertEqual(m.purchase(), "Product out of stock")

    def test_no_balance(self):
        # tests if the user has not entered a balance and tries to purchase
        m = SodaMachine('Coke', 8)
        m.restock(1)
        self.assertEqual(m.purchase(), 'Please deposit $8')

    def test_less_than_enough_balance(self):
        # tests if the program correctly outputs the necessary additional
        # balance to be deposited
        m = SodaMachine('Coke', 8)
        m.restock(1)
        m.deposit(4)
        self.assertEqual(m.purchase(), 'Please deposit $4')

    def test_restock(self):
        # tests if restock() inputs the correct amount of product
        # and if correct message is shown
        m = SodaMachine('Coke', 8)
        self.assertEqual(m.restock(1), 'Current soda stock: 1')
        self.assertEqual(m.stock, 1)

    def test_successful_purchase_no_remaining_balance(self):
        # tests for successful purchase w/o remaining balance
        m = SodaMachine('Coke', 8)
        m.restock(1)
        m.deposit(8)
        self.assertEqual(m.purchase(), 'Coke dispensed')

    def test_successful_purchase_remaining_balance(self):
        # tests for successful purchase with remaining balance
        m = SodaMachine('Coke', 8)
        m.restock(1)
        m.deposit(12)
        self.assertEqual(m.purchase(), 'Coke dispensed, take your $4')
        self.assertEqual(m.Balance, 0)

    def test_deposit_response(self):
        # tests for correct deposit response
        m = SodaMachine('Coke', 8)
        m.restock(1)
        m.deposit(8)
        self.assertEqual(m.purchase(), 'Coke dispensed')

    def test_deposit_variable_setting(self):
        # tests for correct deposit set to class attr.
        m = SodaMachine('Coke', 8)
        m.restock(1)
        m.deposit(1)
        m.deposit(8)
        self.assertEqual(m.Balance, 9)

    def test_deposit_no_stock(self):
        # tests to make sure correct response is shown if user deposits
        # with no available product stock
        m = SodaMachine('Coke', 8)
        self.assertEqual(m.deposit(8), 'Sorry, out of stock. Take your $8 back')

    # ends tests for SodaMachine Class

    def test_distance_one(self):
        # tests that distance fcn calculates distance properly
        line1 = Line((-7,-9),(1,5.6))
        self.assertEqual(line1.distance, 16.648)
    
    def test_distance_two(self):
        # tests another two coords
        line2=Line((2,6),(2,3))
        self.assertEqual(line2.distance, 3.0)

    def test_slope_negative(self):
        # tests for a negative slope
        line1 = Line((-1, -5.6), (-1.2, -5))
        self.assertEqual(line1.slope, -3.0)

    def test_slope_positive(self):
        # tests a positive slope
        line1 = Line((-7, -9), (1, 5.6))
        self.assertEqual(line1.slope, 1.825)

    def test_slope_infinite(self):
        # tests for an infinite slope i.e. if x1 and x2 are ==
        line1 = Line((1,1), (1, 7))
        self.assertEqual(line1.slope, 'Infinity')

if __name__ == '__main__':unittest.main(exit=False)