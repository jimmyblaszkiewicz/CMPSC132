import unittest 
from LAB6 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB6' 
    # test return value for vector
    def test_add_1(self):
        vect = Vector([1,2,3])
        vect2 = Vector([1,3,4])
        self.assertEqual(vect+vect2, Vector([2,5,7]))
    def test_add_dimension_error(self):
        vect = Vector([4,2])
        vect2 = Vector([3])
        self.assertEqual(vect+vect2, 'Error - Invalid dimensions')
    def test_add_operation_error(self):
        vect = Vector([1,2])
        self.assertEqual(vect + 3, 'Error - Invalid operation')

    def test_sub_1(self):
        vect = Vector([1,2,3])
        vect2 = Vector([1,3,4])
        self.assertEqual(vect-vect2, Vector([0,-1,-1]))
    def test_sub_dimension_error(self):
        vect = Vector([4,2])
        vect2 = Vector([3])
        self.assertEqual(vect-vect2, 'Error - Invalid dimensions')
    def test_sub_operation_error(self):
        vect = Vector([1,2])
        self.assertEqual(vect - 3, 'Error - Invalid operation')

    def test_scalar_multiplication(self):
        vect = Vector([1,4,10])
        self.assertEqual(vect * 2, Vector([2,8,20]))
    def test_dot_product(self):
        vect = Vector([1,1,2])
        vect2 = Vector([3, 4, 6])
        self.assertEqual(vect * vect2, 19)
    def test_mul_dimension_1_longer(self):
        vect = Vector([1,2,3,4,5,6,7,8,9,10])
        vect2 = Vector([1,2])
        self.assertEqual(vect * vect2, 5)
    def test_mul_dimension_2_longer(self):
        vect = Vector([3,4])
        vect2 = Vector([1,4,5,6])
        self.assertEqual(vect * vect2, 19)

if __name__ == '__main__':unittest.main(exit=False)