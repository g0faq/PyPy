sp = []
for i in range(8):
    sp.append([int(x) for x in input().split()])
f = False
for elem in sp:
    for element in sp:
        if elem == element:
            continue
        else:
            if elem[0] == element[0] or elem[1] == element[1]:
                print('YES')
                f = True
                break
            elif abs(elem[0] - element[0]) == abs(elem[1] - element[1]):
                print('YES')
                f = True
                break
    if f:
        break

if not f:
    print('NO')