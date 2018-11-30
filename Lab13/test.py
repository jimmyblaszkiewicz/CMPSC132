import unittest 
from LAB13 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'LAB13' 
    def test_MergeSort(self):
        self.assertEqual(mergeSort([12,35,87,26,9,28,7]), [7, 9, 12, 26, 28, 35, 87])
if __name__ == '__main__':unittest.main(exit=False)