__author__ = 'sean'

import voronoi, point, random, pygame
from pygame.locals import *

def main():
    screenrez = (500,500)
    width, height = screenrez
    pygame.init()
    window = pygame.display.set_mode(screenrez)
    pygame.display.set_caption("Voronoi Test")
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    v = voronoi.Voronoi()
    v.screen = screen
    v.pygame = pygame
    v.window = window


    numPoints = 25
    places = []
    for i in range(numPoints):
        randPoint = None
        while not randPoint:
            randPoint = point.Point(random.randint(0, width), random.randint(0,width))
            for existingPoint in places:
                if existingPoint == randPoint:
                    randPoint = None
                    break
            places.append(randPoint)
#    places = [point.Point(random.randint(0, width), random.randint(0,width)) for i in range(numPoints)]
    computed = v.Compute(places, width, height)
    print "finished computing: ", v.cells


if __name__ == '__main__':
    main()