__author__ = 'sean'

import math

class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

def distance(a, b):
    return Math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y-a.y))