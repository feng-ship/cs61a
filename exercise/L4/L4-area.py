def area(r, shape_constant):
    return shape_constant * r * r

def square_area(r):
    return area(r,1)

from math import pi
def circle_area(r):
    return area(r,pi)

from math import sqrt
def hexagon_area(r):
    return area(r,3*sqrt(3)/2)