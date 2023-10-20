import math
from random import random
from matplotlib import pyplot
import time
import numpy
from itertools import combinations

def generate_circle(n, radius, max_noise):
    points = []
    for i in range(n):
        angle = 2 * math.pi * random()
        noise = max_noise * random()
        r = radius * (1 + noise)
        point = [r * math.cos(angle), r * math.sin(angle)]
        points.append(point)
    return points

def plot_points(points, figure=None, radius=0, color='r'):
    xs, ys = map(list, zip(*points))
    pyplot.axis([min(xs)-1, max(xs)+1,min(ys)-1,max(ys)+1])
    pyplot.plot(xs, ys, 'ro')
    if radius > 0:
        if figure is None:
            figure = pyplot.gcf()
        axes = figure.gca()
        for circle in [pyplot.Circle(point, radius, color=color)
                       for point in points]:
            axes.add_artist(circle)
def get_points(points, indices):

    return [points[index] for index in indices]

def draw_triangle(triangle):
    p1, p2, p3 = triangle
    pyplot.plot([p1[0], p2[0]],[p1[1],p2[1]])
    pyplot.plot([p1[0], p3[0]],[p1[1],p3[1]])
    pyplot.plot([p2[0], p3[0]],[p2[1],p3[1]])

def draw_line(line):
    p1, p2 = line
    pyplot.plot([p1[0], p2[0]],[p1[1],p2[1]])

def draw_point(point):
    pyplot.plot(point)

def draw_simplicial_complex(simplices, points):
    handlers = [draw_point, draw_line, draw_triangle]
    for simplex in simplices:
        handlers[len(simplex)-1](get_points(points, simplex))

radius = 0.3
circle = generate_circle(70, 3, radius)
plot_points(circle)

array_circle = numpy.array(circle)

P = [[0,0], [1,0], [0,1]]
A = numpy.array(P, dtype=float)


[list(subset) for subset in combinations(P, 2)]
twoskeleton = []
threeskeleton = []

for subset in combinations(P,2):
    if math.dist(subset[0],subset[1])<=2:
        twoskeleton.append(subset)

for subset in combinations(P,3):
    if math.dist(subset[0],subset[1])<=2 and math.dist(subset[1],subset[2])<=2 and math.dist(subset[0],subset[2])<=2:
        threeskeleton.append(subset)