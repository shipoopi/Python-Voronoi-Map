__author__ = 'sean'
import math

EPSILON = 0.000000001

class Circle:
    p1 = None
    p2 = None
    p3 = None
    def __init__(self, p1, p2, p3):
        self.p1 = (float(p1[0]), float(p1[1]))
        self.p2 = (float(p2[0]), float(p2[1]))
        self.p3 = (float(p3[0]), float(p3[1]))
    def delta(self):
        yDelta_a = self.p2[1] - self.p1[1]
        xDelta_a = self.p2[0] - self.p1[0]
        yDelta_b = self.p3[1] - self.p2[1]
        xDelta_b = self.p3[0] - self.p2[0]
        return (yDelta_a, xDelta_a, yDelta_b, xDelta_b)
    def isPerpendicular(self, p1, p2, p3):
        global EPSILON
        yDelta_a = p2[1] - p1[1]
        xDelta_a = p2[0] - p1[0]
        yDelta_b = p3[1] - p2[1]
        xDelta_b = p3[0] - p2[0]

        if abs(xDelta_a) <= EPSILON and abs(yDelta_b) <= EPSILON:
            return False
        if abs(yDelta_a) <= EPSILON:
            return True
        elif abs(yDelta_b) <= EPSILON:
            return True
        elif abs(xDelta_a) <= EPSILON:
            return True
        elif abs(xDelta_b) <= EPSILON:
            return True
        else:
            return False
    def CalcCircle(self):
        if not self.isPerpendicular(self.p1, self.p2, self.p3):
            return self._circleCheck(self.p1, self.p2, self.p3)
        elif not self.isPerpendicular(self.p1, self.p3, self.p2):
            return self._circleCheck(self.p1, self.p3, self.p2)
        elif not self.isPerpendicular(self.p2, self.p1, self.p3):
            return self._circleCheck(self.p2, self.p1, self.p3)
        elif not self.isPerpendicular(self.p2, self.p3, self.p1):
            return self._circleCheck(self.p2, self.p3, self.p1)
        elif not self.isPerpendicular(self.p3, self.p2, self.p1):
            return self._circleCheck(self.p3, self.p2, self.p1)
        elif not self.isPerpendicular(self.p3, self.p1, self.p2):
            return self._circleCheck(self.p3, self.p1, self.p2)
        else:
            #can't compute
            return None
    def _circleCheck(self, p1, p2, p3):

        global EPSILON
        yDelta_a = p2[1] - p1[1]
        xDelta_a = p2[0] - p1[0]
        yDelta_b = p3[1] - p2[1]
        xDelta_b = p3[0] - p2[0]
        if abs(xDelta_a) <= EPSILON and ABS(yDelta_b) <= EPSILON:
            #simple calculation since it's on a right angle
            x = 0.5 * (p2[0] + p3[0])
            y = 0.5 * (p1[1] + p2[1])
            v = (x - p1[0], y - p1[1])
            r = math.sqrt(v[0] * v[0] + v[1] * v[1])
            return (x,y,r)
    #it's perpendicular, assure deltas are not zero
        aSlope = yDelta_a / xDelta_a
        if aSlope == 0:
            print "aslope is zero"
            print "%d, %d" % p1
            print "%d, %d" % p2
            print "%d, %d" % p3
            exit()
        bSlope = yDelta_b / xDelta_b
        if abs(aSlope - bSlope) <= EPSILON:
            #the 3 points are colinear, can't make a circle
            return None
        #calc center
        x = (aSlope * bSlope *(p1[1] - p3[1]) + bSlope * (p1[0] + p2[0]) - aSlope * (p2[0] + p3[0])) / (2.0 * (bSlope - aSlope))
        y = -1.0 * (x - (p1[0] + p2[0]) / 2.0) / aSlope + (p1[1] + p2[1]) / 2.0
        vx = x - p1[0]
        vy = y - p1[1]
        r = math.sqrt(vx * vx + vy * vy)
        return (x, y, r)

if __name__ == "__main__":
    main()