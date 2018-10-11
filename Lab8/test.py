import unittest 
from LAB8 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'Lab8' 
    def setUp(self):
        self.x = OrderedLinkedList()

    def test_isEmpty_true(self):
        self.assertTrue(self.x.isEmpty)

    def test_isEmpty_false(self):
        self.x.add('A Node')
        self.assertFalse(self.x.isEmpty)

    def test_add(self):
        self.x.add(1)
        self.assertFalse(self.x.isEmpty)

    def test_add_string(self):
        self.x.add('Hello')
        self.x.add('world')
        self.x.add('!')
        self.assertMultiLineEqual(str(self.x), 
            'Head:Node(!)\nTail:Node(world)\nList:! Hello world')
        # exclamation point inserted at beginning bc it has lowest str order

    def test_add_before_head(self):
        self.x.add(10)
        self.x.add(5)
        self.assertMultiLineEqual(str(self.x), 
            'Head:Node(5)\nTail:Node(10)\nList:5 10')

    def test_add_after_head(self):
        self.x.add(1)
        self.x.add(100)
        self.assertMultiLineEqual(str(self.x), 
            'Head:Node(1)\nTail:Node(100)\nList:1 100')

    def test_add_after_tail(self):
        self.x.add(1)
        self.x.add(2)
        self.x.add(50)
        self.assertMultiLineEqual(str(self.x), 
            'Head:Node(1)\nTail:Node(50)\nList:1 2 50')

    def test_add_before_tail(self):
        self.x.add(1)
        self.x.add(2)
        self.x.add(5)
        self.x.add(4)
        self.assertMultiLineEqual(str(self.x),
            'Head:Node(1)\nTail:Node(5)\nList:1 2 4 5')

    def test_pop_returns(self):
        self.x.add(1)
        self.x.add(0)
        self.x.add(-1)
        self.x.add(4)
        self.x.add(3)
        self.x.add(10)
        self.assertEqual(self.x.pop(), 10)

    def test_pop_removes_last(self):
        self.x.add(1)
        self.x.add(2)
        self.x.add(3)
        self.x.pop()
        self.assertEqual(str(self.x), 'Head:Node(1)\nTail:Node(2)\nList:1 2')

    def test_pop_from_one_item_list(self):
        self.x.add(1)
        self.x.pop()
        self.assertEqual(str(self.x), 'Head:None\nTail:None\nList:')
   
    def test_pop_empty(self):
        self.assertEqual(self.x.pop(), 'List is empty')



if __name__ == '__main__':unittest.main(exit=False)