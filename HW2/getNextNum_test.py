import unittest 
from getNextNumber import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'getNextNumber' 
    def test_normal_case(self):
        self.assertEqual(getNextNumber('8  +    5    -2',0), (8.0, '+', 3))

    def test_normal_case_nonzero_pos(self):
        self.assertEqual(getNextNumber('8  +    5    -2',4), (5.0, '-', 13))

    def test_no_next_num(self):
        self.assertEqual(getNextNumber('4.5 + 3.15         /   5',10), (None, '/', 19))

    def test_no_next_operator(self):
        self.assertEqual(getNextNumber('1.2 + 3.5      ', 6), (3.5, None, None))
        
if __name__ == '__main__':unittest.main(exit=False)