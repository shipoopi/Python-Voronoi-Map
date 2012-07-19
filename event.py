__author__ = 'sean'

import random

class Event:
    point = None
    pe = None
    y = 0
    key = None
    arch = None
    value = 0
    def __init__(self, p, pe):
        self.point = p
        self.pe = pe
        self.y = p.y
        self.key = random.random() * 100000000

        self.arch = None
        self.value = 0
    def __eq__(self, other):
        if self.y == other.y and self.key == other.key:
            return True
        return False
    def compare(self, other):
        if self.y > other.y:
            return True
        else:
            return False
    def __str__(self):
        return "%s %f" % (self.point, self.key)
