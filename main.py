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
from point import Point
import circle
import signal, sys

pygame.init()
screenrez = (500,500)
width, height = screenrez
window = pygame.display.set_mode(screenrez)
pygame.display.set_caption("Voronoi")
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
v = Voronoi()


oPoints = [[226,159],[491,21],[490,225],[89,241],[170,152],[180,237],[51,47],[219,326],[472,305],[487,398],[331,235],[365,165],[130,162],[312,89],[242,112]]
events = [Point(p[0], p[1]) for p in oPoints]
heapq.heapify(events)
#points are y,x so they can be ordered by heapq

def input(pyevents):
    global scanline,pygame
    for event in pyevents:
        if event.type == QUIT:
            print "exiting cleanly"
            sys.exit(0)

print events
v.Compute(events, 500,500)
edges = v.edges
for e in edges:
    print "edge: ", e, e.start, e.end
    start = e.start
    end = e.end
#    pygame.draw.line(screen, (255,255,255), (start.x,start.y),(end.x, end.y))
print "edges: ", edges
pygame.display.update()
running = True

def signal_handler(signal, frame):
    print "You pressed Ctrl+C!"
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while running:
    input(pygame.event.get())
    clock.tick(30)



