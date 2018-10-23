import unittest 
from LAB10 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB10' 
    def setUp(self):
        self.q = Queue()

    def test_isEmpty(self):
        self.assertTrue(self.q.isEmpty())

    def test_isEmptyFalse(self):
        self.q.enqueue(1)
        self.assertFalse(self.q.isEmpty())

    def test_enqueue_empty(self):
        self.q.enqueue(1)
        self.assertEqual(str(self.q), 'Head:Node(1)\nTail:Node(1)\nQueue:1')

    def test_enqueue_not_empty(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(15)
        self.assertEqual(str(self.q), 'Head:Node(1)\nTail:Node(15)\nQueue:1 2 15')

    def test_dequeue_empty(self):
        self.assertEqual(self.q.dequeue(), 'Queue is empty')

    def test_dequeue_one_element(self):
        self.q.enqueue(1)
        self.q.dequeue()
        self.assertEqual(str(self.q), 'Head:None\nTail:None\nQueue:')

    def test_dequeue_order(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

        self.assertEqual(self.q.dequeue(), 1)

    def test_dequeue_multiple(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

        self.q.dequeue()
        self.assertEqual(str(self.q), 'Head:Node(2)\nTail:Node(3)\nQueue:2 3')

if __name__ == '__main__':unittest.main(exit=False)