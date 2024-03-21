f = open('26-44_test.txt')
n = int(f.readline())
sp = [int(x) for x in f]
sp.sort()
sp_2 = []
sl = {}

for i in range(21):
    sl[i] = []

for elem in sp:
    sl[(elem - 1) // 500].append(elem)

for i in sl.values():
    print(len(i))

print(sl)

def count_sell(sp):
    count = 0
    for i in range(1, len(sp)):
        if i % 2:
            count += 0.5 * sp[i]
    return count

res = []
res.append(sl[1][0])
for i in range(476):
    res.append(sl[0][i])
    res.append(sl[1][i + 1])

print(res)



sp_2 = sorted(sp)
sp_3 = sorted(sp)[::-1]
res = []
for i in range(n // 2 + 1):
    res.append(sp_2[i])
    res.append(sp_3[i])

print(res)