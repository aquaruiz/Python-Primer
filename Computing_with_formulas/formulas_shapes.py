from math import pi

h = 5  # height
b = 2  # base
r = 1.5  # rаdius

area_parallelipiped = h * b
print("Area of parallelipiped is %.3f" % area_parallelipiped)

area_square = b ** 2
print("Area of square is %g" % area_square)

area_circle = pi * r ** 2
print("Area of circle is %.3f" % area_circle)

area_cone = 1.0 / 3 * pi * r ** 2 * h
print("Area of cone is %.3f" % area_cone)
