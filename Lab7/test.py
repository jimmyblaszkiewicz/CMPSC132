import unittest 
from LAB7 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB7' 
    def test_recursive_triangle_1(self):
        self.assertEqual(recursive_triangle(2,4), '  **\n   *')

    def test_recursive_triangle_5(self):
        self.assertEqual(recursive_triangle(5,5), '*****\n ****\n  ***\n   **\n    *')

    def test_recursive_triangle_4(self):
        self.assertEqual(recursive_triangle(4,4), '****\n ***\n  **\n   *')

    def test_k_greater_than_n(self):
        self.assertEqual(recursive_triangle(5,4), '*****\n****\n ***\n  **\n   *')

if __name__ == '__main__':unittest.main(exit=False)