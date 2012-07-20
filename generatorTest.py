__author__ = 'sean'

import voronoi, point, random, pygame, sys
from pygame.locals import *

pygame.init()
screenrez = (500,500)
window = pygame.display.set_mode(screenrez)
pygame.display.set_caption("Voronoi Test")
screen = pygame.display.get_surface()
clock = pygame.time.Clock()


def drawDiagram(v):
    global screen
    for place in v.places:
        pygame.draw.circle(screen, (128,128,128), (int(place.x), int(place.y)), 5)
    pass

def input(pyevents):
    for event in pyevents:
        if event.type == QUIT:
            sys.exit(0)

def main():
    global screen, pygame, window, screenrez

    width, height = screenrez

    v = voronoi.Voronoi()
    v.screen = screen
    v.pygame = pygame
    v.window = window
    v.clock = clock
    font = pygame.font.Font(None, 16)
    v.font = font


    numPoints = 12
    places = []
    while len(places) < numPoints:
        randPoint = None
        while not randPoint:
            randPoint = point.Point(random.randint(0, width), random.randint(0,width))
            for existingPoint in places:
                if existingPoint.y == randPoint.y:
                    randPoint = None
                    break
            if randPoint:
                places.append(randPoint)
#    places = [point.Point(random.randint(0, width), random.randint(0,width)) for i in range(numPoints)]
    computed = v.Compute(places, width, height)
    print "finished computing: ", v.cells
    for cell in v.cells:
        print "cell: %s" % cell
    while True:
        input(pygame.event.get())
        clock.tick(30)
#        drawDiagram(v)
#        pygame.display.update()


if __name__ == '__main__':
    main()