from math import sin, pi


def simpson(f, a, b, n=500):
    """
    Return the approximation of the integral of f
    from a to b using Simpson's rule with n intervals.
    """

    if a > b:
        print('Error: a=%g > b=%g' % (a, b))
        return None

    # check that n is even:
    if n % 2 != 0:
        print('Error: n=%d is not a even integer!' % n)
        n += 1  # name n even

    h = (b - a) / n
    sum_1 = 0
    for i in range(1, int(n / 2 + 1)):
        sum_1 += f(a + (2 * i - 1) * h)

    sum_2 = 0
    for i in range(1, int(n / 2)):
        sum_2 += f(a + 2 * i * h)

    integral = (b - a) / (3 * n) * (f(a) + f(b) + 4 * sum_1 + 2 * sum_2)
    return integral


def h(x):
    return (3 / 2) * sin(x) ** 3


def application():
    print('Integral of 1.5 * sin ^ 3 from 0 to pi:')
    for n in (2, 6, 12, 100, 500):
        approx = simpson(h, 0, pi, n)
        print('n=%4d, approx=%18.15f, error=%9.2E' % (n, approx, 2 - approx))


application()


def test_simpson():
    """Check that" 2nd-degree polynomials are integrated exactly."""
    a = 1.5
    b = 2
    n = 8
    g = lambda x: 3 * x ** 2 - 7 * x + 2.5  # test integrand
    G = lambda x: x ** 3 - 3.5 * x ** 2 + 2.5 * x  # integral of g
    exact = G(b) - G(a)
    approx = simpson(g, a, b, n)
    success = abs(exact - approx) < 1E-14  # never use == for floats!!!
    msg = 'Cannot integrate a quadratic function exactly!'
    assert success, msg

