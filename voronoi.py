__author__ = 'sean'

import heapq, event, polygon, eventqueue, parabola, point, math, exceptions,sys
from point import Point
from edge import Edge
from pygame.locals import *

class Voronoi:
    places = None
    edges = None
    cells = None
    queue = None
    width = 0
    height = 0
    root = None
    edges = []

    #pygame variables
    pygame = None
    screen = None
    clock = None
    window = None

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
        for place in self.places:
            ev = event.Event(place, True)
            cell = polygon.Polygon()
            self.queue.push(ev)
        loops = 0
        while not self.queue.isEmpty():
            self.loopUntilReady()
            print "loop %d (%d)" % (loops, self.ly)
            e = self.queue.pop(None)
            self.ly = e.y
            if e.pe:
                self.insertParabola(e.point)
            else:
                self.removeParabola(e)
            self.lasty = e.y
            if self.root:
                self.printTree(self.root, 0)
            loops += 1
        print "finishing edge for: " , self.root
        self.finishEdge(self.root)
        for edge in self.edges:
            if edge.neighbor:
                edge.start = edge.neighbor.end

    def insertParabola(self, p):
        if not p:
            raise Exception("p is None")
            exit(-1)
        if not self.root:
            self.root = parabola.Parabola(p.copy())
            self.fp = p.copy()
            return
        if self.root.isLeaf and self.root.site.y - p.y < 0.01:
            self.root.isLeaf = False
            self.root.setLeft(parabola.Parabola(self.fp.copy()))
            self.root.setRight(parabola.Parabola(p.copy()))
            s = Point((p.x + self.fp.x) / 2.0, self.height)
            if p.x > self.fp.x:
                self.root.edge = Edge(s, self.fp.copy(), p.copy())
            else:
                self.root.edge = Edge(s, p, self.fp.copy())
            return
        par = self.getParabolaByX(p.x)
        if par.event:
            self.queue.remove(par.event)
            par.event = None
        start = Point(p.x, self.getY(par.site, p.x))

        e1 = Edge(start, par.site, p)
        er = Edge(start, p, par.site)

        e1.neighbor = er
        self.edges.append(e1)

        par.edge  = er
        par.isLeaf = False

        p0 = parabola.Parabola(par.site.copy())
        p1 = parabola.Parabola(p.copy())
        p2 = parabola.Parabola(par.site.copy())

        par.setRight(p2)
        par.setLeft(parabola.Parabola(None))
        par.left.edge = e1

        par.left.setLeft(p0)
        par.left.setRight(p1)
        print "checking circles"
        self.checkCircle(p0)
        self.checkCircle(p2)

    def checkCircle(self, p):
        print "checking circle for: %s" % p.site
        lp = self.getLeftParent(p)
        rp = self.getRightParent(p)
        print "lp: %s, rp: %s" % (lp, rp)

        a = self.getLeftChild(lp)
        c = self.getRightChild(rp)

        if not a or not c or a.site == c.site:
            print "not a or not c or a.site == c.site"
            return None

        s = self.getEdgeIntersection(lp.edge, rp.edge)
        if not s:
            print "not s"
            return None
        d = point.distance(a.site, s)
        if s.y - d >= self.ly:
            return None

        e = event.Event(Point(s.x, s.y - d), False)
        p.event = e
        e.arch = p
        self.queue.push(e)

    def getEdgeIntersection(self, a, b):
        I = self.getLineIntersection(a.start, a.B, b.start, b.B)
        if not I:
            return None
        #wrong direction of edge
        wd = (I.x - a.start.x) * a.direction.x < 0 or \
                (I.y - a.start.y) * a.direction.y < 0 or \
                    (I.x - b.start.x) * b.direction.x < 0 or \
                        (I.y - b.start.y) * b.direction.y < 0
        if wd:
            return None
        return I

    def getParabolaByX(self, xx):
        par = self.root
        x = 0
        if not par.left and not par.right:
            return par
        while not par.isLeaf:
            x = self.getXofEdge(par, self.ly)
            if x > xx:
                par = par.left
            else:
                par = par.right
        return par

    def getXofEdge(self, par, y):
        left = self.getLeftChild(par)
        right = self.getRightChild(par)

        p = left.site
        r = right.site

        dp = 2.0 * (float(p.y) - float(y))
        if dp == 0:
            print "degenerate parabola"
            #degenerate parabola
            return p.x
        a1 = 1.0 / dp
        b1 = -2.0 * p.x / dp
        c1 = y+dp * 0.25 + p.x * p.x / dp
        dp = 2.0 * (float(r.y) - float(y))
        if dp == 0:
            print "degenerate parabola"
            return r.x
        a2 = 1.0 / dp
        b2 = -2.0 * r.x / dp
        c2 = y+dp * 0.25 + r.x * r.x / dp

        a = a1-a2
        b = b1-b2
        c = c1-c2

        disc = b*b - 4.0 * a * c
        x1 = (-1.0 * b + math.sqrt(disc)) / (2.0 * a)
        x2 = (-1.0 * b - math.sqrt(disc)) / (2.0 * a)

        ry = None
        if p.y < r.y:
            ry = max((x1, x2))
        else:
            ry = min((x1, x2))
        return ry

    def removeParabola(self, e):
        print "removing parabola"
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
        if p0.site and p0.site.cell:
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
            par = par.parent
            if par == x1:
                higher = x1
            if par == xr:
                higher = xr
        higher.edge = Edge(p, p0.site, p2.site)

        self.edges.append(higher.edge)

        gparent = p1.parent.parent
        if p1.parent.left == p1:
            if gparent.left == p1.parent:
                gparent.setLeft(p1.parent.right)
            else:
                p1.parent.parent.setRight(p1.parent.right)
        else:
            if gparent.left == p1.parent:
                gparent.setLeft(p1.parent.left)
            else:
                gparent.setRight(p1.parent.left)
        self.checkCircle(p0)
        self.checkCircle(p2)


    def finishEdge(self, n):
        mx = None
        if n.edge.direction.x > 0.0:
            mx = max((self.width, n.edge.start.x + 10))
        else:
            mx = min((0.0, n.edge.start.x - 10))
        n.edge.end = Point(mx, n.edge.f*mx + n.edge.g)
        print "n: ", n
        if not n.left.isLeaf:
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
        px = p.x
        py = p.y
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
        try:
            while not par.isLeaf:
                par = par.right
        except exceptions.AttributeError:
            pass
        finally:
            return par
    def getRightChild(self, n):
        if not n:
            return None
        par = n.right
        try:
            while not par.isLeaf:
                par = par.left
        except exceptions.AttributeError:
            pass
        finally:
            return par
    def getLineIntersection(self, a1, a2, b1, b2):
        dax = a1.x - a2.x
        dbx = b1.x - b2.x
        day = a1.y - a2.y
        dby = b1.y - b2.y

        Den = dax*dby - day*dbx
        if Den == 0:
            print "parallel"
            return None #parallel
        A = (a1.x * a2.y - a1.y * a2.x)
        B = (b1.x * b2.y - b1.y * b2.x)

        I = Point(0,0)
        I.x = (A*dbx - dax*B) / Den
        I.y = (A*dby - day*B) / Den
        return I
    def printTree(self, p, depth = None):
        """print the binary tree starting from this point"""
        try:
            curDepth = int(depth)
        except exceptions.TypeError as e:
            curDepth = 0
        finally:
            padding = " " * curDepth
        print "%s%s" % (padding, p)
        if p.left:
            print padding + "left"
            self.printTree(p.left, depth+1)
        if p.right:
            print padding + "right:"
            self.printTree(p.right, depth+1)
#
    def numAligned(self, p):
        numAligned = 0
        for place in self.places:
            if p.y == place.y:
                numAligned += 1
        return numAligned

    def loopUntilReady(self):
        self.drawFunction()
        screen = self.screen
        pygame = self.pygame
        clock = self.clock
        ready = False
        while not ready:
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
                elif e.type == KEYDOWN:
                    ready = True
            clock.tick(30)
    def drawTree(self, p):
        if p.isLeaf:
            screen = self.screen
            width = screen.get_width()
            height = screen.get_height()
            pygame = self.pygame
            if p.site.y == self.ly:
                #draw a line going straight up (degenerate parabola)
                pass
            else:
                #draw the full parabola
                arc = []
                for x in range(width):
                    y = self.getY(p.site, x)
                    arc.append((x,y))
                pygame.draw.lines(screen, (200,200,200), False, arc, 1)


        else:
            if p.left:
                self.drawTree(p.left)
            if p.right:
                self.drawTree(p.right)
    def drawFunction(self):
        screen = self.screen
        width = screen.get_width()
        height = screen.get_height()
        screen.fill((0,0,0))
        pygame = self.pygame
        font = self.font


        pygame.draw.line(screen, (128,0,0), (0,self.ly), (width, self.ly))
        for place in self.places:
            color = (128,128,128)
            pygame.draw.circle(screen, color, (int(place.x), int(place.y)), 3)
            textSurface = font.render(str(place), 1, color)
            textPos = (int(place.x + 3),int(place.y))
            screen.blit(textSurface, textPos)


        allEvents = self.queue.getAll()
#        for e in allEvents:
#            color = (0,255,0)
#            if not e.pe:
#                color = (255,0,0)
#            pygame.draw.circle(screen, color, (int(e.point.x), int(e.point.y)), 3)
        #now walk the tree
        if self.root:
            self.drawTree(self.root)

        pygame.display.update()