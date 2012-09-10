__author__ = 'sean'
from Point import Point

class VEdge:
    def __init__(self, s, a, b):
        self.left = a
        self.right = b
        self.start = s
        self.end = None

        self.f = (b.x - a.x) / (a.y - b.y)
        self.g = s.y - self.f * s.x
        self.direction = Point(b.y-a.y, -(b.x-a.x))
        self.B = Point(s.x + self.direction.x, s.y + self.direction.y)

        self.interesected = False
        self.iCounted = False
        self.neighbour = None