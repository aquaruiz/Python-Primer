from math import sqrt

for n in range(1, 60):
    r = 2
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2

    print('%d times sqrt and ** 2: %.16f' % (n, r))