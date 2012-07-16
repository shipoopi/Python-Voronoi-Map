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
points = []
#points are y,x so they can be ordered by heapq
def generatePoints():
    global points
    points = [(int(random.random() * width), int(random.random() * height)) for i in range(numPoints)]
generatePoints()

heapq.heapify(points)
print points
EPSILON = 0.005

pygame.key.set_repeat(100,30)
def input(events):
    global scanline
    for event in events:
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
        else:
            pass

def generate_diagram():
    global scanline, screen, width, height, points
    v.ly = scanline
#    point = (250,300)
    screen.fill((0,0,0))
    vertices = []
    #draw the line
    pygame.draw.line(screen, (128,0,0), (0, scanline), (width, scanline))
    for point in points:
        py, px = point
        pygame.draw.circle(screen, (128,128,128), (px, py), 3)
        if py < scanline:
            #draw the arc
            arc = []
            for x in range(width):
                arcy = int(v.getY((px, py), x))
                if arcy >= 0 and arcy < 500:
                    arc.append((x, arcy))
            pygame.draw.lines(screen, (255,255,255), False, arc, 1)










while True:
    input(pygame.event.get())
    clock.tick(30)
    generate_diagram()
    pygame.display.update()



def mag(a, b):
    return math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1], 2))



