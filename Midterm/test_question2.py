import unittest 
from question2 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'question2' 
    def test_distance1(self):
        p1 = Point2D(-7,-9)
        p2 = Point2D(1, 5.6)
        line1 = Line(p1, p2)
        self.assertEqual(line1.distance, 16.648)

    def test_distance2(self):
        p1 = Point2D(-7,-9)
        p2 = Point2D(1, 5.6)
        line1 = Line(p1, p2)
        self.assertEqual(line1.midpoint, (-3.0, -1.7))

    def test_distance_3D(self):
        p1 = Point3D(1,2,3)
        p2 = Point3D(4,5,5)
        line1 = Line(p1,p2)
        self.assertEqual(line1.distance, 4.69)

    def test_midpoint_3D(self):
        p1 = Point3D(1,2,3)
        p2 = Point3D(4,5,5)
        line1 = Line(p1,p2)
        self.assertEqual(line1.midpoint, "({}, {}, {})".format(2.5, 3.5, 4.0))


if __name__ == '__main__':unittest.main(exit=False)