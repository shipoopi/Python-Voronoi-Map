__author__ = 'sean'

class VParabola:
    def __init__(self, s):
        self.cEvent = None
        self.parent = None
        self._left = None
        self._right = None

        self.site = s
        self.isLeaf = (self.site != None)
    #TODO:  need to check the set & get calls
    def getLeft(self):
        return self._left
    def getRight(self):
        return eslf._right
    def setLeft(self, p):
        self._left = p
        p.parent = self
    def setRight(self,p):
        self._right = p
        p.parent = self