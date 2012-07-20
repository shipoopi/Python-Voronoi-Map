__author__ = 'sean'

import random

class Parabola:
    def __init__(self, site):
        self.event = None
        self.parent = None
        self.left = None
        self.right = None
        self.site = site
        self.id = random.randint(0, 1000000)
        self.isLeaf = self.site != None
        edge = None
    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False
    def __str__(self):
        isLeaf = ""
        if self.isLeaf:
            isLeaf = 'leaf'
        return "Parabola: %d (%s) %s" % (self.id, self.site, isLeaf)
    def __ne__(self, other):
        return not self.__eq__(other)
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setLeft(self, p):
        self.left = p
        p.parent = self
    def setRight(self, p):
        self.right = p
        p.parent = self
