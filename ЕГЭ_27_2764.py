f = open('27B_2764.txt')
n = int(f.readline())
sp = [int(x) for x in f]

sp_1 = [[] for _ in range(23)]
for elem in sp:
    sp_1[elem % 23].append([elem, sp.index(elem)])

res = 10 ** 100
for x in range(1, 12):
    for i in range(len(sp_1[x])):
        for j in range(len(sp_1[-x])):
            if (sp_1[x][i][0] * sp_1[-x][j][0]) % 6 == 0:
                if abs(sp_1[x][i][1] - sp_1[-x][j][1]) >= 7:
                    res = min(res, sp_1[x][i][0] + sp_1[-x][j][0])

print(res)