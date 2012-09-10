__author__ = 'sean'

from VQueue import VQueue
from VEvent import VEvent
from VPolygon import VPolygon
import sys
class Voronoi:
    def __init__(self):
        self.places = None
        self.edges = None
        self.cells = None
        self.queue = VQueue()

        self.width = 0
        self.height = 0
        self.root = None
        self.ly = 0
        self.lasty = 0
        self.fp = None
    def Compute(self, p, width, height):
        if len(p) < 2:
            return []
        self.root = None
        self.places = p
        self.edges = []
        self.cells = []
        self.width = width
        self.height = height
        self.queue.clear()

        for p in self.places:
            ev = VEvent(p, True)
            cell = VPolygon()
            p.cell = cell
            self.queue.enqueue(ev)
            self.cells.append(cell)

        lasty = sys.float_info.max
        num = 0
        while not self.queue.isEmpty():
            e = self.queue.dequeue()
            self.ly = e.point.y
            if e.pe:
                self.InsertParabola(e.point)
            else:
                selfl.RemoveParabola(e)
            self.lasty = e.y
        self.FinishEdge(self.root)
        for e in self.edges:
            if e.neighbour:
                e.start = e.neighbour.end
    def GetEdges(self):
        return self.edges
    def GetCells(self):
        return self.cells

    #METHODS TO WORK WITH THE TREE
    
    def InsertParabola(self, p):
        #TODO:  write function
        pass
    def RemoveParabola(self, e):
        #TODO:  write function
        pass
    def FinishEdge(self, e):
        #TODO:  write function
        pass
