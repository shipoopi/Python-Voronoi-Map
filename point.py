__author__ = 'sean'

import math

EPSILON = 0.000000001
class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.cell = None
        self.x = float(x)
        self.y = float(y)
    def __eq__(self, other):
        difY = other.y - self.y
        difX = other.x - self.x
        if difY > -1.0 * EPSILON and difY < EPSILON:
            if difX > -1.0 * EPSILON and difX < EPSILON:
                return True
        return False
    def __str__(self):
        return "[%d,%d]" % (self.x, self.y)
    def copy(self):
        new = Point(self.x, self.y)
        return new

def distance(a, b):
    return math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y-a.y))