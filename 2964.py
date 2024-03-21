def F(n, m, table):
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                table[i][j] = -1
            else:
                table[i][j] = 0

    if table[0][0] == -1:
        return 'Impossible'

    table[0][0] = 1
    for i in range(1, m):
        if table[0][i] != -1 and table[0][i - 1] != -1:
            table[0][i] += table[0][i - 1]

    for i in range(1, n):
        if table[i][0] != -1 and table[i - 1][0] != -1:
            table[i][0] += table[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if table[i][j] != -1:
                if table[i - 1][j] != -1:
                    table[i][j] += table[i - 1][j]
                if table[i][j - 1] != -1:
                    table[i][j] += table[i][j - 1]

    if table[n - 1][m - 1] <= 0:
        return 'Impossible'
    return table[n - 1][m - 1]


a, b = map(int, input().split())
table_1 = []
for _ in range(a):
    table_1.append(list(map(int, input().split())))

print(F(a, b, table_1))