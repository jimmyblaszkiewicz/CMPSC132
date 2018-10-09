import unittest 
from LAB8 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'Lab8' 
    def setUp(self):
        self.x = OrderedLinkedList()

    def test_isEmpty(self):
        
        self.assertTrue(self.x.isEmpty)

    def test_add(self):
        self.x.add(1)
        self.assertFalse(self.x.isEmpty)

    def test_pop_returns(self):
        self.x.add(1)
        self.x.add(2)
        self.x.add(3)
        self.assertEqual(str(self.x.pop()), str(Node(1)))

    def test_pop_removes_last(self):
        self.x.add(1)
        self.x.add(2)
        self.x.add(3)
        popped = self.x.pop()
        self.assertEqual(len(self.x), 2)

    def test_pop_empty(self):
        self.assertEqual(self.x.pop(), 'List is empty')


if __name__ == '__main__':unittest.main(exit=False)