a = 2; b = 1; c = 2
from cmath import sqrt
q = b * b - 4 * a * c
q_sr = sqrt(q)
x_1 = (- b + q_sr) / 2 * a
x_2 = (- b - q_sr) / 2 * a
print(x_1, x_2)