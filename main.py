#!/usr/bin/python
__author__ = 'sean'

from PIL import Image
import random
import math
import pygame, sys
import random
import heapq
from pygame.locals import *
from voronoi import Voronoi
import circle

pygame.init()
screenrez = (500,500)
width, height = screenrez
window = pygame.display.set_mode(screenrez)
pygame.display.set_caption("Voronoi")
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
v = Voronoi()

scanline = 0
numPoints = 12
events = []
points = []
#points are y,x so they can be ordered by heapq
def randColour():
    return (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))
def generatePoints():
    global events, points
    points = [(int(random.random() * width), int(random.random() * height), randColour()) for i in range(numPoints)]
    events = [(point[0], point[1], 's') for point in points]
    heapq.heapify(events)
generatePoints()

print events
EPSILON = 0.005

pygame.key.set_repeat(100,30)
def input(pyevents):
    global scanline,pygame
    for event in pyevents:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                scanline += 1
            elif event.key == K_UP:
                scanline -= 1
            elif event.key == K_r:
                generatePoints()
                scanline = 1
            if scanline >= 500:
                scanline = 0
            elif scanline < 0:
                scanline = 500
            generate_diagram()
            pygame.display.update()
        else:
            pass

beach = []
def generate_diagram():
    global scanline, screen, width, height, events, points
    v.ly = scanline
#    point = (250,300)
    screen.fill((0,0,0))
    vertices = []
    #draw the line
    pygame.draw.line(screen, (128,0,0), (0, scanline), (width, scanline))
    circles = []
    currentPoint = 0
    prev = None
    prevPrev = None
    for point in points:
        py, px, pColour = point
        if py == scanline:
            pygame.draw.line(screen, pColour, (px, scanline), (px, 0))
        elif py < scanline:
            arc = []
            for x in range(width):
                arcy = v._getY((px, py), x)
                arc.append((x, arcy))
            pygame.draw.lines(screen, pColour, False, arc, 1)
        if py <= scanline:
            if prev and prevPrev:
                c = circle.Circle(prev, prevPrev, (px, py))
                circles.append(c)
            prevPrev = prev
            prev = (px, py)

    for c in circles:
        calculated = c.CalcCircle()
        if calculated:
            cx, cy, r = calculated
            pygame.draw.circle(screen, (200, 200, 200), (int(cx), int(cy)), int(r), 1)
    for point in points:
        py, px, pColour = point
        pygame.draw.circle(screen, pColour, (px, py), 3)

#    while len(events) != 0:
#        smallest = heapq.heappop(events)
#        ey, ex, etype = smallest
#        if etype == 's':
#            #site event
#            pass
#        else:
#            #circle/vertex event
#            pass
generate_diagram()
pygame.display.update()

while True:
    input(pygame.event.get())
    clock.tick(30)





def mag(a, b):
    return math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1], 2))



