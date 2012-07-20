__author__ = 'sean'

from point import Point
class Edge:
    left = None
    right = None
    start = None
    end = None
    f = None
    g = None
    direction = None
    B = None
    intersected = False
    iCounted = False
    neighbor = None
    def __init__(self, s, a, b):
        self.left = a
        self.right = b
        self.start = s
        self.end = None

        self.f = (b.x - a.x) / (a.y - b.y)
        self.g = s.y - self.f * s.x
        self.direction = Point(b.y - a.y, -1.0 * (b.x - a.x));
        self.B = Point(s.x + self.direction.x, s.y + self.direction.y) #second point of line

        self.intersected = False
        self.iCounted = False

        self.neighbor = None
    def __str__(self):
        return "%s -> %s" % (self.start, self.direction)