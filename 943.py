n = int(input())

sp = []
for i in range(n):
    sp.append([0] * (i + 1))
    sp[i][0] = sp[i][-1] = 1
    if i > 1:
        for j in range(1, len(sp[i]) - 1):
            sp[i][j] = sp[i - 1][j] + sp[i - 1][j - 1]

for elem in sp:
    print(*elem)