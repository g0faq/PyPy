f = open('26-44.txt')
n = int(f.readline())
sp = [int(x) for x in f]
sp.sort()
sp_2 = []
sl = {}

for i in range(20):
    sl[i] = []

for elem in sp:
    sl[(elem - 1) // 500].append(elem)

res = []
for i in range(20):
    for j in range(1, len(sl[i]) // 2 + 1):
        res.append(sl[i][-j])
        res.append(sl[i][j - 1])
    if len(sl[i]) % 2 != 0:
        res.append(sl[i][len(sl[i]) // 2])
    if len(sl[i]) % 2 != 0:
        del res[-1]

res_count, res_max = 0, 0
for i in range(1, len(res), 2):
    if (res[i] - 1) // 500 == (res[i - 1] - 1) // 500:
        res_count += res[i] / 2
        res_max = res[i] // 2

print(int(res_count), res_max)