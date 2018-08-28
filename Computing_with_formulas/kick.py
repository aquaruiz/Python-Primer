from math import pi

ro = 1.2  # density og air in kg m-3
a = 11  # football ball radius in cm
a = a / 100  # football ball radius in m
A = pi * a ** 2  # cross-section area
m = 0.43  # mass in kg
c_d = 0.2  # drag coefficient
g = 9.81  # gravity in ms-2

v = 0  # velocity

f_d = 1 / 2 * (c_d * ro * A * v ** 2)  # drag force
f_g = m * g  # gravity force
ratio = f_d / f_g
print("Drag force %.1f kg m / s2" % f_d)
print("Drag force %.1f kg m / s2" % f_g)
print("Drag force to Gravity Force ratio %.2f\n" % ratio)

v = 120  # velocity hard kick in km/h
v = v * 1000 / 3600  # velocity in m/s
f_d = 1 / 2 * (c_d * ro * A * v ** 2)  # drag force
f_g = m * g  # gravity force
ratio = f_d / f_g
print("Drag force %.1f kg m / s2" % f_d)
print("Gravity force %.1f kg m / s2" % f_g)
print("Drag force to Gravity Force ratio %.2f\n" % ratio)

v = 10  # velocity soft kick in km/h
v = v * 1000 / 3600  # velocity in m/s
f_d = 1 / 2 * (c_d * ro * A * v ** 2)  # drag force
f_g = m * g  # gravity force
ratio = f_d / f_g
print("Drag force %.1f kg m / s2" % f_d)
print("Gravity force %.1f kg m / s2" % f_g)
print("Drag force to Gravity Force ratio %.2f" % ratio)
