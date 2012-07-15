#!/usr/bin/python
__author__ = 'sean'

from PIL import Image
import random
import math
import pygame, sys
import random
import heapq
from pygame.locals import *

pygame.init()
screenrez = (500,500)
width, height = screenrez
window = pygame.display.set_mode(screenrez)
pygame.display.set_caption("Voronoi")
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

scanline = 0
numPoints = 12

#points are y,x so they can be ordered by heapq
points = [(int(random.random() * width), int(random.random() * height)) for i in range(numPoints)]
heapq.heapify(points)
print points

pygame.key.set_repeat(100,30)
def input(events):
    global scanline
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            scanline += 1
            if scanline >= 500:
                scanline = 0
        else:
            pass

def generate_diagram():
    global scanline, screen, width, height, points
#    point = (250,300)
    screen.fill((0,0,0))
    vertices = []
    while len(points) != 0:
        first = None
        for point in points:
            first = point
            #if it's a site event
                #AddParabola(point)
            #else:
                #RemoveParabola(point)
            break




while True:
    input(pygame.event.get())
    clock.tick(30)
    pygame.display.update()
    generate_diagram()


def mag(a, b):
    return math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1], 2))



generate_diagram()
