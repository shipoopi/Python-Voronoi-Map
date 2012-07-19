__author__ = 'sean'

import voronoi, point, random

def main():
    width, height = (500,500)
    v = voronoi.Voronoi()
    numPoints = 25
    places = [point.Point(random.randint(0, width), random.randint(0,width)) for i in range(numPoints)]
    computed = v.Compute(places, width, height)

if __name__ == '__main__':
    main()