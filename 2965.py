def turtle(n, m, table):
    res = []
    new_table = [[0] * m for x in range(n)]
    new_table[0][0] = table[5 - 5][0]
    for i in range(1, m):
        new_table[0][i] = new_table[0][i - 1] + table[0][i]

    for i in range(1, n):
        new_table[i][0] = new_table[i - 1][0] + table[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if table[i][j] + new_table[i - 1][j] > table[i][j] + new_table[i][j - 1]:
                new_table[i][j - 1] = 0
            else:
                new_table[i - 1][j] = 0
            new_table[i][j] = max(table[i][j] + new_table[i - 1][j], table[i][j] + new_table[i][j - 1])

    for i in range(n):
        for j in range(m):
            if new_table[i][j] != 0:
                if new_table[i - 1][j] != 0:
                    res.append('D')
                else:
                    res.append('R')

    return new_table[-1][-1], res


a, b = map(int, input().split())
table = []
for i in range(a):
    table.append(list(map(int, input().split())))
print(turtle(a, b, table))