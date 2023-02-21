pyareas
=======
A simple Python library for finding the areas of 2D shapes
----------------------------------------------------------
Shapes Included:
----------------
- Square
- Triangle
- Rectangle
- Circle
- Parellelogram
- Ellipse
- Rhombus
- Trapezoid
- Polygon(regular)
- Kite
- Star

Install command:
----------------
```
pip install pyareas
```

Example:
--------
```
from pyareas import *

print(Square(10))
```
Gives the output:
```
100
```
Newest Feature:
---------------
- Star!
- Takes the arguments of the internal shape's side, the internal shape's apothem, the number of points on the star, and the height of the triangles(the points)
- The old functions of pentagram, hexagram and heptagram are still in the source code, but i thought i would add a function for all stars.

To do:
------
- Add more shapes
- Create a new library for volume of 3D shapes
	- pyvolumes?
	- pyareas3d?
