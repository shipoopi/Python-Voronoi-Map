__author__ = 'sean'

class Parabola:
    def __init__(self, site):
        self.event = None
        self.parent = None
        self.left = None
        self.right = None
        self.site = site
        self.isLeaf = self.site != None
        edge = None
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.event == other.event:
                return self.__dict__ == other.__dict__
        else:
            return False
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
