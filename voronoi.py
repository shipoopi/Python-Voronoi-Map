__author__ = 'sean'

import heapq, event, polygon, eventqueue, parabola, point
from point import Point
from edge import Edge

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
            e = self.queue.pop(None)
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
            if edge.neighbor:
                edge.start = edge.neighbor.end

    def insertParabola(self, p):
        if not self.root:
            self.root = parabola.Parabola(p)
            self.fp = p
            return
        if self.root.isLeaf and self.root.site.y - p.y < 0.01:
            self.root.isLeaf = false
            self.root.left = parabola.Parabola(self.fp)
            self.root.right = parabola.Parabola(p)
            s = Point((p.x + self.fp.x) / 2.0, self.height)
            if p.x > self.fp.x:
                self.root.edge = Edge(s, self.fp, p)
            else:
                self.root.edge = Edge(s, p, self.fp)
            return
        par = self.getParabolaByX(p.x)
        if par.event:
            self.queue.pop(par.event)
            par.event = None
        start = Point(p.x, self.getY(par.site, p.x))

        e1 = Edge(start, par.site, p)
        er = Edge(start, p, par.site)

        e1.neighbor = er
        self.edges.append(e1)

        par.edge  = er
        par.isLeaf = False

        p0 = parabola.Parabola(par.site)
        p1 = parabola.Parabola(p)
        p2 = Parabola.Parabola(par.site)

        par.right = p2
        par.left = Parabola(None)
        par.left.edge = e1

        par.left.left = p0
        par.left.right = p1

        self.checkCircle(p1)
        self.checkCircle(p2)
        self.checkCircle(p2)

    def checkCircle(self, p):
        lp = self.getLeftParent(p)
        rp = self.getRightParent(p)

        a = self.getLeftChild(lp)
        c = self.getRightChild(rp)

        if not a or not c or a.site == c.site:
            return None

        s = self.getEdgeIntersection(lp.edge, rp.edge)
        if not s:
            return None
        d = point.distance(a.site, s)
        if s.y - d >= self.ly:
            return None

        e = event.Event(Point(s.x, s.y - d), false)
        b.event = e
        e.arch = b
        self.queue.push(e)

    def getEdgeIntersection(self, a, b):
        I = self.getLineIntersection(a.start, a.B, b.start, b.B)

        #wrong direction of edge
        wd = (I.x - a.start.x) * a.direction.x < 0 or \
                (I.y - a.start.y) * a.direction.y < 0 or \
                    (I.x - b.start.x) * b.direction.x < 0 or \
                        (I.y - b.start.y) * b.direction.y < 0
        if wd:
            return None
        return I

    def getParabolaByX(self, x):
        pass
        #TODO:  define getParabolaByX

    def removeParabola(self, e):
        p1 = e.arch

        x1 = self.getLeftParent(p1)
        xr = self.getRightParent(p1)

        p0 = self.getLeftChild(x1)
        p2 = self.getRightChild(xr)

        if p0.event:
            self.queue.remove(p0.event)
            p0.event = None
        if p2.event:
            self.queue.remove(p2.event)
            p2.event = None

        p = Point(e.point.x, self.getY(p1.site, e.point.x))
        if p0.site.cell.last == p1.site.cell.first:
            p1.site.cell.addLeft(p)
        else:
            p1.site.cell.addRight(p)
        p0.site.cell.addRight(p)
        p2.site.cell.addLeft(p)

        self.lasty = e.point.y

        higher = None
        par = p1
        while par != self.root:
            par = parent
            if par == x1:
                higher = x1
            if par == xr:
                higher = xr
        higher.edge = Edge(p, p0.site, p2.site)

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
        self.checkCircle(p0)
        self.checkCircle(p2)


    def finishEdge(self, n):
        mx = None
        if n.edge.direction.x > 0.0:
            mx = max((self.width, n.edge.start.x + 10))
        else:
            mx = min((0.0, n.edge.start.x - 10))
        n.edge.end = Point(mx, n.edge.f*mx + n.edge.g)

        if not n.leaf.isLeaf:
            self.finishEdge(n.left)
        if not n.right.isLeaf:
            self.finishEdge(n.right)
    def getY(self, p, x):
        dp = 2.0 * (p.y - self.ly)
        b1 = -2.0 * p.x / dp
        c1 = self.ly + dp / 4.0 + p.x * p.x / dp
        return (x*x/dp + b1*x  + c1)

    def _getY(self, p, x):
        """deprected"""
        px, py = p
        dp = 2.0 * (py - self.ly)
        a1 = 1.0 / dp
        b1 = -2.0 * px / dp
        c1 = self.ly + dp / 4 + px * px / dp
        return a1*x*x + b1*x + c1
    def getLeft(self, n):
        return self.getLeftChild(self.getLeftParent(n))
    def getRight(self, n):
        return self.getRightChild(self.getRightParent(n))
    def getLeftParent(self, n):
        par = n.parent
        pLast = n
        while par.left == pLast:
            if not par.parent:
                return None
            pLast = par
            par = par.parent
        return par
    def getRightParent(self, n):
        par = n.parent
        pLast = n
        while par.right == pLast:
            if not par.parent:
                return None
            pLast = par
            par = par.parent
        return par
    def getLeftChild(self, n):
        if not n:
            return None
        par = n.left
        while not par.isLeaf:
            par = par.right
        return par
    def getRightChild(self, n):
        if not n:
            return None
        par = n.right
        while not par.isLeaf:
            par = par.left
        return par
    def getLineIntersection(self, a1, a2, b1, b2):
        dax = a1.x - a2.x
        dbx = b1.x - b2.x
        day = a1.y - a2.y
        dby = b1.y - b2.y

        Den = dax*dby - day*dbx
        if Den < point.EPSILON:
            return None #parallel
        A = (a1.x * a2.y - a1.y * a2.x)
        B = (b1.x * b2.y - b1.y * b2.x)

        I = Point(0,0)
        I.x = (A*dbx - dax*B) / Den
        I.y = (A*dby - day*B) / Den
        return I
