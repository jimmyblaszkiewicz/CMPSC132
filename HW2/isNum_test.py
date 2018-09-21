import unittest 
from isNumber import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'isNumber  
    def test_float(self):
        self.assertTrue(isNumber('1.3'))

    def test_int(self):
        self.assertTrue(isNumber(1))

    def test_string(self):
        self.assertFalse(isNumber('Not a number'))

    def test_spaced_num(self):
        self.assertFalse(isNumber('1.4 2'))


if __name__ == '__main__':unittest.main(exit=False)