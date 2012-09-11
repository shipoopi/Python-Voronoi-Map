__author__ = 'sean'

from ported.VParabola import VParabola
from VQueue import VQueue
from VEvent import VEvent
from VPolygon import VPolygon
from VEdge import VEdge
from Point import Point, distance
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
        if not self.root:
            self.root = VParabola(p)
            self.fp = p
            return None
        if self.root.isLeaf and self.root.site.y - p.y < 0.01:
            #degenerated parabola
            self.root.isLeaf = False
            self.root.left = VParabola(self.fp)
            self.root.right = VParabola(p)
            s = Point((p.x + self.fp.x) / 2.0, self.height)
            if p.x > self.fp.x:
                self.root.edge = VEdge(s, self.fp, p)
            self.edges.append(self.root.edge)
            return None

        par = self.getParabolaByX(p.x)

        if par.cEvent:
            self.queue.remove(par.cEvent)
            par.cEvent = None

        start = Point(p.x, self.GetY(par.site, p.x))

        el = VEdge(start, par.site, p)
        er = VEdge(start, p, par.site)
        #TODO:  REST OF FUNCTION
    def RemoveParabola(self, e):
        p1 = e.arch

        xl = self.GetLeftParent(p1)
        xr = self.GetRightParent(p1)

        p0 = self.GetLeftChild(xl)
        p2 = self.GetRightChild(xr)

        if p0.cEvent:
            self.queue.remove(p0.cEvent)
            p0.cEvent = None
        if p2.cEvent:
            self.queue.remove(p0.cEvent)
            p2.cEvent = None

        p = Point(e.point.x, self.GetY(p1.site, e.point.x))
        #TODO:  comparison of points is not implemented?
        if p0.site.cell.last == p1.site.cell.first:
            p1.site.cell.addLeft(p)
        else:
            p1.site.cell.addRight(p)

        p0.site.cell.addRight(p)
        p2.site.cell.addLeft(p)

        self.lasty = e.point.y

        xl.edge.end = p
        xr.edge.end = p

        higher = None
        par = p1
        while par != self.root:
            par = par.parent
            if par == xl:
                higher = xl
            if par == xr:
                higher = xr

        higher.edge = VEdge(p, p0.site, p2.site)

        self.edges.append(higher.edge)

        gparent = p1.parent.parent
        if p1.parent.left == p1:
            if gparent.left == p1.parent:
                gparent.left = p1.parent.right
            else:
                p1.parent.parent.right = p1.parent.right
        else:
            if gparent.left == p1.parent:
                gparent.left = p1.parent.left
            else:
                gparent.right = p1.parent.left
        self.CheckCircle(p0)
        self.CheckCircle(p2)
    def FinishEdge(self, n):
        mx = None
        if n.edge.direction.x > 0.0:
            mx = max((self.width, n.edge.start.x + 10))
        else:
            mx = min((0.0, n.edge.start.x - 10))
        n.edge.end = Point(mx, n.edge.f * mx + n.edge.g)
        if not n.left.isLeaf:
            self.FinishEdge(n.left)
        if not n.right.isLeaf:
            self.FinishEdge(n.right)
    def getXOfEdge(self, par, y):
        left = self.getLeftChild(par)
        right = self.GetRightChild(par)
        p = left.site
        r = right.site

        dp = 2.0 * (p.y - y)
        a1 = 1.0 / dp
        b1 = -2.0 * p.x / dp
        c1 = y + dp * 0.25 + p.x * p.x / dp

        dp = 2.0 * (r.y - y)
        a2 = 1.0 / dp
        b2 = -2.0 * r.x / dp
        c2 = y + dp * 0.25 + r.x * r.x / dp

        a = a1 - a2
        b = b1 - b2
        c = c1 - c2

        disc = b * b - 4 * a * c
        x1 = (-b + math.sqrt(disc)) / (2.0 * a)
        x2 = (-b - math.sqrt(disc)) / (2.0 * a)

        ry = None
        if p.y < r.y:
            ry = max((x1,x2))
        else:
            ry = min((x1,x2))
        return ry

    def getParabolaByX(self, xx):
        par = self.root
        x = 0
        while not par.isLeaf:
            x = self.getXOfEdge(par, self.ly)
            if x > xx:
                par = par.left
            else:
                par = par.right
        return par
    def GetY(self, p, x):
        dp = 2.0 * (p.y - self.ly)
        b1 = -2.0 * p.x / dp
        c1 = self.ly + dp / 4.0 + p.x * p.x / dp
        return x*x / dp + b1 * x + c1
    def CheckCircle(self, b):
        lp = self.GetLeftParent(b)
        rp = self.GetRightParent(b)
        a = self.GetLeftChild(lp)
        c = self.GetRightChild(rp)

        if not a or not c or a.site == c.site:
            return None
        d = distance(a.site, s)
        if s.y - d >= self.ly:
            return
        e = Event(Point(s.x, s.y - d), False)
        b.cEvent = e
        e.arch = b
        self.queue.enqueue(e)
    def GetEdgeIntersection(self, a, b):
        I = self.GetLineIntersection(a.star, a.B, b.start, b.B)
        #wrong direction of edge
        wd = (I.x - a.start.x) * a.direction.x < 0 \
            or (I.y - a.start.y) * a.direction.y < 0 \
                or (I.x - b.start.x) * b.direction.x < 0 \
                    or (I.y - b.start.y) * b.direction.y < 0
        if wd:
            return None
        return I
    def GetLeft(self, n):
        return self.GetLeftChild(self.GetLeftParent(n))
    def GetRight(self, n):
        return self.GetRightChild(self.GetRightParent(n))
    def GetLeftParent(self, n):
        par = n.parent
        pLast = n
        while par.left == pLast:
            if not par.parent:
                return None
            pLast = par
            par = par.parent
        return par
    def GetRightParent(self, n):
        par = n.parent
        pLast = n
        #TODO:  need to write comparison function
        while par.right == pLast:
            if not par.parent:
                return None
            pLast = par
            par = par.parent
        return par
    def GetLeftChild(self, n):
        if not n:
            return None
        par = n.left
        while not par.isLeaf:
            par = par.right
        return par
    def GetRightChild(self, n):
        if not n:
            return None
        par = n.right
        while not par.isLeaf:
            par = par.left
        return par
    def GetLineIntersection(self, a1, a2, b1, b2):
        dax = (a1.x - a2.x)
        dbx = (b1.x - b2.x)
        day = a1.y - a2.y
        dby = b1.y - b2.y
        Den = dax*dby - day * dbx
        if Den == 0:
            return None
        A = (a1.x * a2.y - a1.y - a2.x)
        B = b1.x * b2.y - b1.y * b2.x
        I = Point(0,0)
        I.x = (A * dbx - B * dax) / Den
        I.y = (A * dby - B * day) / Den
        return I

