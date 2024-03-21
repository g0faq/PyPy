f = open('27B_7879.txt')
n = int(f.readline())
k = int(f.readline())
sp = [int(x) for x in f]

res = 0

sp_1 = [[] for _ in range(2023)]
for elem in sp:
    sp_1[elem % 2023].append([elem, sp.index(elem)])

for x in range(1, 2023 // 2 + 1):
    e1 = sp_1[x]
    e2 = sp_1[-x]
    for i in range(len(e1)):
        for j in range(len(e2)):
            if e1[i][0] % 47 == 0 or e2[j][0] % 47 == 0:
                if abs(e1[i][1] - e2[j][1]) >= k:
                    res = max(res, e1[i][0] + e2[j][0])

print(res)
