m, n = map(int, input().split())
sp = []
l = []

for i in range(m):
    l = [x for x in input().split()]
    for elem in l:
        sp.append(elem)

sl = {}
for elem in sp:
    if elem not in sl:
        sl[elem] = sp.count(elem)

#print(sl)

if (m * n) % 2 == 0:
    f = False
    for key in sl:
        if sl[key] % 2 == 0:
            f = False
        else:
            f = True
        if f:
            print('NO')
            break
        else:
            print('YES')
            break
else:
    count = 0
    for key in sl:
        if sl[key] % 2 == 1:
            count += 1
            print(count)
    if count == 1:
        print('YES')
    else:
        print('NO')
