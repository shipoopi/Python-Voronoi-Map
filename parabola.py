__author__ = 'sean'

class Parabola:
    def __init__(self, site):
        self.event = None
        self.parent = None
        self._left = None
        self._right = None
        self.site = site
        self.isLeaf = not self.site
    def getLeft(self):
        return self._left
    def getRight(self):
        return self._right
    def setLeft(self, p):
        self._left = p
        p.parent = self
    def setRight(self, p):
        self._right = p
        p.parent = self