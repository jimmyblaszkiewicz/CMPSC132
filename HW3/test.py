import unittest 
from HW3 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'HW3' 

    # addition tests
    def test_simple_addition(self):
        self.assertEqual(calculator('2+31'), 33)
    def test_simple_addition_spaces(self):
        self.assertEqual(calculator('2 +  3 '), 5)
    def test_multiple_addition(self):
        self.assertEqual(calculator('1+2+3'), 6)
    def test_multiple_addition_spaces(self):
        self.assertEqual(calculator('1 +   50 +  7 '), 58)

    # multiplication tests
    def test_simple_multiplication(self):
        self.assertEqual(calculator('2*3'), 6)
    def test_simple_multiplication_spaces(self):
        self.assertEqual(calculator('2 * 3  '), 6)
    def test_multiple_multiplication(self):
        self.assertEqual(calculator('2*3*2'), 12)
    def test_multiple_multiplication_spaces(self):
        self.assertEqual(calculator('2 * 3 *   21'), 126 )

    # subtraction tests
    def test_simple_subtraction(self):
        self.assertEqual(calculator('2-6'), -4)
    def test_simple_subtraction_spaces(self):
        self.assertEqual(calculator(' 2  - 7  '), -5)
    def test_multiple_subtraction(self):
        self.assertEqual(calculator('2-6-20'), -24)
    def test_multiple_subtraction_spaces(self):
        self.assertEqual(calculator('2 - 15      - 8'), -21)

    # division tests
    def test_simple_division(self):
        self.assertEqual(calculator('1/2'), 0.5)
    def test_simple_division_spaces(self):
        self.assertEqual(calculator('  1   /  4'), 0.25)
    def test_multiple_division(self):
        self.assertEqual(calculator('1/2/2'), 0.25)
    def test_multiple_division_spaces(self):
        self.assertEqual(calculator('1  / 2       / 4'), .125)

    # simple combinations
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

    # mixed combinations
    def test_mixed_one(self):
        self.assertEqual(calculator('4*3-2/2'), 11)
    def test_mixed_two(self):
        self.assertEqual(round(calculator('23 / 12 - 223 + 5.25 * 4 * 3423'), 4), 71661.9167)
    def test_mixed_three(self):
        self.assertEqual(calculator('-2 - 3*4'), -14)
    def test_mixed_four(self):
        self.assertEqual(round(calculator('-4 * 2/2*6'), 4), -24)
    def test_mixed_five(self):
        self.assertEqual(calculator('-28.0  / 4 * 4'), -28)
    
    # error handling tests
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

    # exponents simple combinations
    def test_simple_exponents(self):
        self.assertEqual(calculator('2^2'), 4)
    def test_add_then_exp(self):
        self.assertEqual(calculator('1+2^3'), 9)
    def test_exp_then_add(self):
        self.assertEqual(calculator('2^3-1'), 7)
    def test_mul_then_exp(self):
        self.assertEqual(calculator('2*3^4'), 162)
    def test_mul_exp_by_zero(self):
        self.assertEqual(calculator('0*2^4'), 0)

    # multiple combinations
    def test_mul_then_exp_then_add(self):
        self.assertEqual(calculator('2*3^4-1'), 161)
    def test_add_then_exp_then_mul(self):
        self.assertEqual(calculator('2+2^3*10'), 82)
    def test_mul_exp_mul(self):
        self.assertEqual(calculator('3*2^4/2'), 24)
    def test_add_exp_add(self):
        self.assertEqual(calculator('3+2^3+40'), 51)

    # many different exponents and complex combinations
    def test_multiple_with_exp(self):
        self.assertEqual(calculator('2  +   3^4 * 5^3   -   10 * 2^10   +   112^1'), -1)
    def test_exp_zero(self):
        self.assertEqual(calculator('2^0 * 100'), 100)
    def test_mixed_with_exp_1(self):
        self.assertEqual(round(calculator('-5 + 60 / 3^3 * 4 - 2 * 4 ^2'),2), -28.11)
    def test_mixed_with_exp_2(self):
        self.assertEqual(calculator('5*3 + 2^1'), 17) 
    def test_mixed_with_exp_3(self):
        self.assertEqual(round(calculator('5^6 * 2/45 +98 - 61^2'), 4), -2928.5556)
    def test_mixed_with_exp_4(self):
        self.assertEqual(calculator('2*2^100'), calculator('2^101'))
        
if __name__ == '__main__':unittest.main(exit=False)