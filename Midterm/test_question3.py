import unittest 
from question3 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'question3' 
    def test_add(self):
        a = Complex(1,2)
        b = Complex(-2,5)
        self.assertEqual(a+b, Complex(-1, 7))

    '''
    todo: fix this later so it looks like a real unittest
    '''
    
if __name__ == '__main__':unittest.main(exit=False)