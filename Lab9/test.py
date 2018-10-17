import unittest 
from LAB9 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB9' 
    def setUp(self):
        self.x = Stack()

    def test_isempty_true(self):
        self.assertTrue(self.x.isEmpty)

    def test_isempty_false(self):
        self.x.push(1)
        self.assertFalse(self.x.isEmpty)

    def test_push_num(self):
        self.x.push(1)
        self.x.push(2)
        self.assertEqual(str(self.x), 'Top:Node(2)\nStack:\n2\n1')

    def test_pop_several(self):
        self.x.push(1)
        self.x.push(2)
        self.x.push(3)

        self.assertEqual(self.x.pop(), 3)
        self.assertEqual(self.x.pop(), 2)

    def test_peek(self):
        self.x.push(1)
        self.assertEqual(self.x.peek(), 1)

    def test_length_maintenance(self):
        self.assertEqual(len(self.x), 0)
        self.x.push(1)
        self.assertEqual(len(self.x), 1)
        self.x.push(2)
        self.assertEqual(len(self.x), 2)
        self.x.pop()
        self.assertEqual(len(self.x), 1)

    def test_pop_empty(self):
        self.assertEqual(self.x.pop(), 'Stack is empty')

    def test_peek_empty(self):
        self.assertEqual(self.x.peek(), 'Stack is empty')



if __name__ == '__main__':unittest.main(exit=False)