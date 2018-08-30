q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]


for row in q:  # find is there 'a'
    if 'a' in row:
        print('a is in %s' % row)
        break

if ['d', 'e', 'f'] in q:  # find is there ['d', 'e', 'f']
    print("['d', 'e', 'f'] is in q")

print(q[-1][-1])  # print last last element

for row in q:  # find is there 'a'
    if 'd' in row:
        print('d is in %s' % row)
        break

print(q[-1][-2])  # last row but before last element

for i in q:
    for j in range(len(i)):
        print(i[j])
