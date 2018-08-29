n = int(input())
v0 = 1
g = 9.81
n += 1
dt = 2 * v0 / g / (n - 1)

t = [i * dt for i in range(0, n)]
y = [v0 * t[i] - 0.5 * g * t[i] ** 2 for i in range(0, n)]

print('%7s %7s' % ('t', 'y'))
for t_val, y_val in zip(t, y):
    print('%7.3f %7.3f' % (t_val, y_val))