n = int(input())
v0 = 1
g = 9.81
n += 1
dt = 2 * v0 / g / (n - 1)

print('%7s %7s' % ('t', 'y'))

for i in range(n):
    t = i * dt
    y = v0 * t - g * t ** 2 / 2
    print('%7.3f %7.3f' % (t, y))
