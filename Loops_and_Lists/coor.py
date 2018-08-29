n = int(input())

a = 0
b = 100
h = (b - a) / n
list = []

for element in range(n + 1):
    x = a + element * h
    list.append(x)

print(list)

list = [a + e * h for e in range(n + 1)]
print(list)
