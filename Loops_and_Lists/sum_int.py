n = int(input())

f_sum = n * (n + 1) / 2

sum = 0
for element in range(n + 1):
    sum += element

print(sum, int(f_sum))