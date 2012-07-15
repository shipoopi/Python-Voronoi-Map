__author__ = 'sean'
from Callable import Callable

class Parabola:
    isLeaf = False
    site = None
    edge = None
    event = None
    parent = None
    _left = None
    _right = None
    def setLeft(self, p):
        self._left = p
        p.parent = self
    def setRight(self, p):
        self._right = p
        p.parent = self;
    def left(self):
        return _left;
    def right(self):
        return _right;

    #static functions
    def GetLeft(p):
        pass
    GetLeft = Callable(GetLeft)

    def GetRight(p):
        pass
    GetRight = Callable(GetRight)

    def GetLeftParent(p):
        pass
    GetLeftParent = Callable(GetLeftParent)

    def GetRightParent(p):
        pass
    GetRightParent = Callable(GetRightParent)

    def GetLeftChild(p):
        pass
    GetLeftChild = Callable(GetLeftChild)

    def GetRightChild(p):
        pass
    GetRightChild = Callable(GetRightChild)
