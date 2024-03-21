def F(n, m):
    table = [[0] * m for _ in range(n)]
    table[0][0] = 1
    for i in range(n):
        for j in range(m):
            if table[i][j] != 0:
                if i + 2 < n and j + 1 < m:
                    table[i + 2][j + 1] += table[i][j]
                if i + 1 < n and j + 2 < m:
                    table[i + 1][j + 2] += table[i][j]
    return table[n - 1][m - 1]


a, b = map(int, input().split())
print(F(a, b))