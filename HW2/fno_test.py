import unittest 
from findNextOpr import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'findNextOpr' 
    def test_findNextOperator_0(self):
        self.assertEqual(findNextOpr("- 1 2 3 4 +"), 0)

    def test_findNextOperator_1(self):
        self.assertEqual(findNextOpr("0-1"), 1)

    def test_findNextOperator_none(self):
        self.assertEqual(findNextOpr("8888888"), -1)

    def test_findNextOperator_empty(self):
        self.assertEqual(findNextOpr(""), 'type error: findNextOpr')


    
if __name__ == '__main__':unittest.main(exit=False)