from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log

def trapezint_1(f, a, b):
    f_x = (b - a) / 2 * (f(a) + f(b))
    return f_x


f1 = (cos, 0, pi)
f2 = (sin, 0, pi)
f3 = (sin, 0, pi / 2)

functions = [f1, f2, f3]


def verify(f, a, b):
    exact = quad(f, a, b)[0]
    approx = trapezint_1(f, a, b)
    error = abs(exact - approx)
    print('The exact integral of %s between %.5f and %.5f is %.5f.'
          '\n\r'
          'The approximate answer is %.5f giving an error of %.5f'
          % (f.__name__, a, b, exact, approx, error))


for f in functions:
    verify(f[0], f[1], f[2])

print()


def trapezint_2(f, a, b):
    return (b - a) / 4. * (f(a) + 2 * f((a + b) / 2) + f(b))


def verify_2(f, a, b):
    exact = quad(f, a, b)[0]
    approx = trapezint_2(f, a, b)
    error = abs(exact - approx)
    print('The exact integral of %s between %.5f and %.5f is %.5f.'
          '\n\r'
          'The approximate answer is %.5f giving an error of %.5f'
          % (f.__name__, a, b, exact, approx, error))


for f in functions:
    verify_2(f[0], f[1], f[2])


print()


def trapezint_3(f, a, b, n):
    h = (b - a) / n
    f_x = 0
    for i in range(n):
        x_i = (a + i * h)
        x_i_1 = a + (i + 1) * h
        f_x += 1/2 * h * (f(x_i) + f(x_i_1))
    return f_x