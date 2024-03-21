n, m = map(int, input().split())

sp = [[0] * n for i in range(m)]
sp[0][0] = 1

for i in range(1, n):
    sp[0][i] += sp[0][i - 1]

for i in range(1, m):
    sp[i][0] += sp[i - 1][0]

for i in range(1, m):
    for j in range(1, n):
        sp[i][j] += sp[i - 1][j] + sp[i][j - 1]

print(sp[m - 1][n - 1])