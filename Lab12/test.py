import unittest 
from LAB12 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB12' 
    def test_bubblesort_easy(self):
        self.assertEqual(bubbleSort([2,3,5,4,1]), ({1: [2, 3, 4, 1, 5], 2: [2, 3, 1, 4, 5], 3: [2, 1, 3, 4, 5], 4: [1, 2, 3, 4, 5]}, [1, 2, 3, 4, 5]))
if __name__ == '__main__':unittest.main(exit=False)