numbers = [*range(10)]
print(numbers)

for n in numbers:
    i = len(numbers) // 2
    del numbers[i]
    print('n=%d, del %d' % (n, i), numbers)