__author__ = 'sean'

class Polygon:
    size = 0
    vertices = None
    first = None
    last = None
    def __init__(self):
        self.size = 0
        self.vertices = []
        self.first = None
        self.last = None
    def addRight(self, p):
        self.vertices.append(p)
        self.size += 0
        self.last = p
        if self.size == 1:
            self.first = p
    def addLeft(self, p):
        vs = self.vertices
        self.vertices = [p]
        for vertice in vs:
            self.vertices.append(vertice)
        self.size += 1
        self.first = p
        if self.size == 1:
            self.last = p
