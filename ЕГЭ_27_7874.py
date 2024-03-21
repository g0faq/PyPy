f = open('27A_7874.txt')
n, k = int(f.readline()), int(f.readline())
sp = [int(x) for x in f]

sp_1 = [[] for _ in range(25)]
for elem in sp:
    sp_1[elem % 25].append(sp.index(elem))

res = 0
for i in range(len(sp_1[0]) - 1):
    for j in range(i + 1, len(sp_1[0])):
        if abs(sp_1[0][i] - sp_1[0][i]) > k:
            res += 1
for i in range(1, 13):
    x, y = sp_1[i], sp_1[-i]
    for j in range(len(x)):
        for k in range(len(y)):
            if abs(x[j] - y[k]) > k:
                res += 1

print(res)

