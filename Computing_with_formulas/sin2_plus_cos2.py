from math import sin, cos, pi

x = pi / 4
val = sin(x) ** 2 + cos(x) ** 2
print(val)
# sin2(x) + cos2(x) = 1 ?

v0 = 3  # m/s
t = 1  # s
a = 2  # m/s2
s = v0 * t + 0.5 / a * t ** 2  # m
print(s)

a = 3.3
b = 5.3
a2 = a ** 2
b2 = b ** 2

eq1_sum = a ** 2 + 2 * a * b + b ** 2
eq2_sum = a ** 2 - 2 * a * b + b ** 2
eq1_pow = (a + b) ** 2
eq2_pow = (a - b) ** 2

print("First equation: %g = %g" % (eq1_sum, eq1_pow))
print("Second equation: %g = %g" % (eq2_sum, eq2_pow))
