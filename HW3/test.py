import unittest 
from HW3 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'HW3' 
    def test_simple_addition(self):
        self.assertEqual(calculator('2+31'), 33)
    def test_simple_addition_spaces(self):
        self.assertEqual(calculator('2 +  3 '), 5)
    def test_multiple_addition(self):
        self.assertEqual(calculator('1+2+3'), 6)
    def test_multiple_addition_spaces(self):
        self.assertEqual(calculator('1 +   50 +  7 '), 58)


    def test_simple_multiplication(self):
        self.assertEqual(calculator('2*3'), 6)
    def test_simple_multiplication_spaces(self):
        self.assertEqual(calculator('2 * 3  '), 6)
    def test_multiple_multiplication(self):
        self.assertEqual(calculator('2*3*2'), 12)
    def test_multiple_multiplication_spaces(self):
        self.assertEqual(calculator('2 * 3 *   21'), 126 )

    def test_simple_subtraction(self):
        self.assertEqual(calculator('2-6'), -4)
    def test_simple_subtraction_spaces(self):
        self.assertEqual(calculator(' 2  - 7  '), -5)
    def test_multiple_subtraction(self):
        self.assertEqual(calculator('2-6-20'), -24)
    def test_multiple_subtraction_spaces(self):
        self.assertEqual(calculator('2 - 15      - 8'), -21)

    def test_simple_division(self):
        self.assertEqual(calculator('1/2'), 0.5)
    def test_simple_division_spaces(self):
        self.assertEqual(calculator('  1   /  4'), 0.25)
    def test_multiple_division(self):
        self.assertEqual(calculator('1/2/2'), 0.25)
    def test_multiple_division_spaces(self):
        self.assertEqual(calculator('1  / 2       / 4'), .125)

    def test_multiply_then_add(self):
        self.assertEqual(calculator('2*2+1'), 5)
    def test_multiply_then_sub(self):
        self.assertEqual(calculator('-2*2-5'), -9)

    def test_add_then_multiply(self):
        self.assertEqual(calculator('2+2*4'), 10)
    def test_sub_then_multiply(self):
        self.assertEqual(calculator('2-2*4'), -6)

    def test_add_then_divide(self):
        self.assertEqual(calculator('2+2/4'), 2.5)
    def test_sub_then_divide(self):
        self.assertEqual(calculator('2-2/4'), 1.5)

    def test_mixed_one(self):
        self.assertEqual(calculator('4*3-2/2'), 11)
    def test_mixed_two(self):
        self.assertEqual(round(calculator('23 / 12 - 223 + 5.25 * 4 * 3423'), 4), 71661.9167)
    def test_mixed_three(self):
        self.assertEqual(calculator('-2 - 3*4'), -14)
    def test_mixed_four(self):
        self.assertEqual(round(calculator('-4 * 2/2*6'), 4), -24)

    def test_starts_with_negative_then_div(self):
        self.assertEqual(calculator('-28.0  / 4 * 4'), -28)
    

    def test_error_lineA(self):
        self.assertEqual(calculator(""), 'input error line A: calculator')
    def test_error_lineB(self):
        self.assertEqual(calculator('+'), 'input error line B: calculator')
    def test_error_ends_in_operator(self):
        self.assertEqual(calculator('3 + 2 -4 *10 +'), 'error: line ends in operator')
    def test_too_many_numbers(self):
        self.assertEqual(calculator('2 3 4 54 +1'), 'error: no operator between numbers')
    def test_too_many_operators(self):
        self.assertEqual(calculator('2 + / 5'), 'error: no number between operators')

if __name__ == '__main__':unittest.main(exit=False)