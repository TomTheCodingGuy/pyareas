##Areas of basic 2d shapes
##TomTheCodingGuy
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
    return area

def Kite(height,width):
    area=(height*width)/2
    return area

def Pentagram(pentside,pentapothem,triheight):
    triangles = (pentside*triheight/2)*5
    pent = Polygon(5,pentside,pentapothem)
    area = triangles + pent
    return area

def Hexagram(hexside,hexapothem,triheight):
    triangles = (hexside*triheight/2)*6
    hexa = Polygon(6,hexside,hexapothem)
    area = triangles + hexa
    return area

def Heptagram(heptside,heptapothem,triheight):
    triangles = (heptside*triheight/2)*7
    hept = Polygon(7,heptside,heptapothem)
    area = triangles + hept
    return areas

def Star(shapeside,shapeapothem,points,triheight):
    triangles = (shapeside*triheight/2)*points
    shape = Polygon(points,shapeside,shapeapothem)
    area = triangles + shape
    return area