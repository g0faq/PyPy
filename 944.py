n, m = map(int, input().split())
n, m = m, n
sp = []

for i in range(m):
    sp.append(list(map(int, input().split())))

table = [[0] * n for _ in range(m)]
table[0][0] = sp[0][0]

for i in range(1, n):
    table[0][i] = table[0][i - 1] + sp[0][i]

for i in range(1, m):
    table[i][0] = table[i - 1][0] + sp[i][0]

for i in range(1, m):
    for j in range(1, n):
        table[i][j] = min((sp[i][j] + table[i - 1][j]), (sp[i][j] + table[i][j - 1]))

print(table[m - 1][n - 1])
