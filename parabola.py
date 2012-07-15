__author__ = 'sean'
from Callable import Callable

class Parabola:
    isLeaf = False
    site = 0
    edge = 0
    event = 0
    parent = 0
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
        return Parabola.GetLeftChild(Parabola.GetLeftParent(p))
    GetLeft = Callable(GetLeft)

    def GetRight(p):
        return Parabola.GetRightChild(Parabola.GetRightParent(p))
    GetRight = Callable(GetRight)

    def GetLeftParent(p):
        parent = p.parent
        pLast = p
        while p.left() == pLast:
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

    def FromParabola(p):
        p = Parabola()
        p.site = p
        p.isLeaf = True
        p.event = 0
        p.parent = 0
        return p
    FromParabola = Callable(FromParabola)
