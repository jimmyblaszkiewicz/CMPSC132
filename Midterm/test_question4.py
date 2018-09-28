import unittest 
from question4 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'question4' 
    
    def test_recursive_power1(self):
        self.assertEqual(power(3,4), 81)

    def test_recursive_power2(self):
        self.assertEqual(power(4,2), 16)

    def test_recursive_power3(self):
        self.assertEqual(power(2,6), 64)

    def test_recursive_power4(self):
        self.assertEqual(power(2,7), 128)


if __name__ == '__main__':unittest.main(exit=False)