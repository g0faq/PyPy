f = open('26-k6_test.txt')
n, k = map(int, f.readline().split())
sp = [list(map(int, x.split())) for x in f]

sl = {}
cost = []

for elem in sp:
    if elem[1] // elem[0] not in sl:
        sl[elem[1] // elem[0]] = []
        cost.append(elem[1] // elem[0])
    sl[elem[1] // elem[0]].append(elem[0])

cost.sort()
count = 0
total = 0
ma = [0, 0]

for elem in cost:
    sl[elem].sort(reverse=True)

for elem in cost:
    for element in sl[elem]:
        count += 1
        total += element
        if elem > ma[0]:
            ma[0] = element
            ma[1] = elem * element
        if count == k:
            break
    if count == k:
        break

print(total, ma[1])
