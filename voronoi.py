__author__ = 'sean'

import heapq, event, polygon, eventqueue

class Voronoi:
    places = None
    edges = None
    cells = None
    queue = None
    width = 0
    height = 0
    root = None
    edges = []

    ly = 0
    lasty = 0
    fp = None
    def __init__(self):
        edges = 0
        ly = 0
        self._clearQueue()
    def _clearQueue(self):
        self.queue = eventqueue.EventQueue()

    def Compute(self, p, width, height):
        if len(p) < 2:
            return ()
        self.root = None
        self.places = p
        self.edges = []
        self.cells = []
        self.width = width
        self.height = height
        self._clearQueue()
        for place in places:
            ev = event.Event(place, True)
            cell = polygon.Polygon()
            place.cell = cell
            self.queue.push(ev)
        while not self.queue.isEmpty():
            e = self.queue.pop()
            self.ly = e.y
            if e.pe:
                self.insertParabola(e.point)
            else:
                self.removeParabola(e)
            self.lasty = e.y
        self.finishEdge(self.root)
        for edge in self.edges:
            #TODO:  continue on Voronoi.prototype.Compute
            # from http://blog.ivank.net/voronoi-diagram-in-javascript.html

    def insertParabola(self, p):
        pass
    def removeParabola(self, e):
        pass
    def finishEdge(self, root):
        pass


    def getY(self, p, x):
        px, py = p
        dp = 2.0 * (py - self.ly)
        a1 = 1.0 / dp
        b1 = -2.0 * px / dp
        c1 = self.ly + dp / 4 + px * px / dp
        return a1*x*x + b1*x + c1
