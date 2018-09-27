import unittest 
from LAB6 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB6' 
    # test return value for vector
    def test_repr(self):
        vect = Vector([1,2,3])
        self.assertEqual(print(vect), "Vector([1,2,3])")

    
if __name__ == '__main__':unittest.main(exit=False)