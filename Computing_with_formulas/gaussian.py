from math import pi, exp, sqrt

m = 0
s = 2
x = 1

f_x = (1 / (sqrt(2 * pi) * s)) * exp((- 1 / 2) * ((x - m) / s) ** 2)
print(f_x)