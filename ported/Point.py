__author__ = 'sean'

import math
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def distance(self, a, b):
        #TODO:  need to check if this is called correctly
        return math.sqrt((b.x - a.x) * (b.x-a.x) + (b.y - a.y) * (b.y-a.y))