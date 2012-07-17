__author__ = 'sean'

class Parabola:
    def __init__(self, site):
        self.event = None
        self.parent = None
        self._left = None
        self._right = None
        self.site = site
        self.isLeaf = not self.site
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
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