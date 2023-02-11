##Areas of basic 2d shapes
##Thomas B
import math

def Square(side):
    area = side * side
    return area

def Rectangle(side1,side2):
    area = side1 * side2
    return area

def Triangle(base,height):
    area = (base/2) * height
    return area

def Circle(radius):
    pi = math.pi
    rSquared = radius * radius
    area = pi * rSquared
    return area

def Parellelogram(base, perpendicularHeight):
    area = base * perpendicularHeight
    return area

def Trapezoid(base, parellelSide, height):
    area = (base+parellelSide)/2 * height
    return area

def Ellipse(majorRadius, minorRadius):
    area = majorRadius * minorRadius * math.pi
    return area

def Rhombus(height,width):
    area = (height*width)/2
    return area

def Polygon(sides,sidelength,apothem):
    perimeter=sidelength*sides
    area=(perimeter*apothem)/2
    return areas