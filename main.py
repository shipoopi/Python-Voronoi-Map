#!/usr/bin/python
__author__ = 'sean'

from PIL import Image
import random
import math
import pygame, sys
import random
from pygame.locals import *

pygame.init()
screenrez = (500,500)
width, height = screenrez
window = pygame.display.set_mode(screenrez)
pygame.display.set_caption("Voronoi")
screen = pygame.display.get_surface()
scanline = 0
numPoints = 12
points = [(int(random.random() * width), int(random.random() * height)) for i in range(numPoints)]
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

    pygame.draw.line(screen, (255,0,0), (0,scanline),(width,scanline))

    for point in points:
        pygame.draw.circle(screen, (128,128,128), (point[0],point[1]),1)
        pointlist = []
        safeToDraw = True
        if point[1] > scanline:
            for x in range(width):
                dp = 2.0 * (point[1] - scanline)
                if dp == 0:
                    safeToDraw = False
                    continue
                a1 = 1.0 / dp
                b1 = -2.0 * point[0] / dp;
                c1 = scanline + dp / 4 + point[0] * point[0] / dp;
                y = int(a1 * x * x + b1 * x + c1)
                pointlist.append((x,y))
            if safeToDraw:
                pygame.draw.lines(screen, (255,255,255), False, pointlist, 1)




clock = pygame.time.Clock()
while True:
    input(pygame.event.get())
    clock.tick(30)
    pygame.display.update()
    generate_diagram()


def mag(a, b):
    return math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1], 2))



generate_diagram()
