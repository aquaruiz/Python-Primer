def convert_fahrenheit_to_celsius(f):
    c = 5 / 9 * (f - 32)
    return c


def f(c):
    f = 9 / 5 * c + 32
    return f


c = 30
success = convert_fahrenheit_to_celsius(f(c)) - c < 1e-16
msg = 'Wrong!!!'
assert success, msg