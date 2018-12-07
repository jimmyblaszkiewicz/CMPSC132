import unittest 
from LAB14 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB14' 
    def test_makingsound(self):
        catSound = makingSound(6, "Meow")
        self.assertEqual(catSound(10), ['Meow', 1, 2, 3, 4, 5, 'Meow', 7, 8, 9])
    def test_makingsound_again(self):
        self.assertEqual(makingSound(6, 'Meow')(10), ['Meow', 1, 2, 3, 4, 5, 'Meow', 7, 8, 9])
    def test_vectorizing_squares(self):
        self.assertEqual(vectorizing(lambda x: x**2)([1,2,3,4,5]), [1,4,9,16,25])

if __name__ == '__main__':unittest.main(exit=False)