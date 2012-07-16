__author__ = 'sean'

class Voronoi:
    edges = 0
    ly = 0
    def __init__(self):
        edges = 0

    def getEdges(self, v, w, h):
        """get the edges"""
        pass
    def getY(self, p, x):
        px, py = p
        dp = 2.0 * (py - self.ly)
        a1 = 1.0 / dp
        b1 = -2.0 * px / dp
        c1 = self.ly + dp / 4 + px * px / dp
        return a1*x*x + b1*x + c1
