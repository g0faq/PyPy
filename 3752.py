s = [int(x) for x in input().split()]
v = []
for elem in s:
    if elem in v:
        print('YES')
    else:
        print('NO')
    v.append(elem)