'''
James Blaszkiewicz
CMPSC 132 Midterm
Question 2
Create a Point2D class to emulate a point with 2 coordinates in x and y
Create a Point3D class to emulate a point with 3 coordinates in x, y, z

Create a Line class which has 2 end points, 
each instances of either Point2D or Point3D

Create property methods of Line class distance and midpoint
that return the length of the line and the midpoint of the line, respectively
'''

# need sqrt from math
from math import sqrt

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # 2 dimensional points have z=0, no matter what
        # this makes calculations for midpoint and distance easier
        self.z = 0

    def __repr__(self):
        # because z is 0, no need to display in the return
        return "({}, {})".format(self.x, self.y)


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # return 3 coords
        return "({}, {}, {})".format(self.x, self.y, self.z)


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @property
    def midpoint(self):
        # the two points will have x and y values regardless of whether or not
        # they are 3d
        midX = round((self.point1.x + self.point2.x)/2, 3)
        midY = round((self.point1.y + self.point2.y)/2, 3)

        # keeping this calculation inside an if makes sure if both are 2D
        # no wasted calculation for z1 = 0, z2 = 0
        if isinstance(self.point1, Point3D) or isinstance(self.point2, Point3D):
            midZ = round((self.point1.z + self.point2.z)/2, 3)
            return Point3D(midX, midY, midZ)

        return Point2D(midX, midY)

    @property
    def distance(self):
        # if either point is 3D, do 3D calculations
        if isinstance(self.point1, Point3D) or isinstance(self.point2, Point3D):
            distance = sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2 + (self.point1.z - self.point2.z)**2)

        # otherwise, ignore z
        else:
            distance = sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)

        return round(distance, 3)
    



