def my_sum(lis):
    s = 0

    for el in lis:
        if type(el) == str:
            s = ''
            break
        elif type(el) == list:
            s = []
            break

    for el in lis:
        s += el
    return s


print(my_sum([1, 3, 5, -5]))
print(my_sum([[1, 2], [4, 3], [8, 1]]))
print(my_sum(['Hello, ', 'World!']))
