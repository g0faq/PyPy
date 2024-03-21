def F(n, m):
    while True:
        f = False
        for i in range(n):
            for j in range(m):
                if table[i][j] > 0:

                    if i < 0 and j < m - 2:
                        table[i - 1][j + 2] -= table[i][j]
                        f = True

                    if i < n - 1 and j < m - 2:
                        table[i + 1][j + 2] += table[i][j]
                        f = True

                    if i < n - 2 and j < m - 1:
                        table[i + 1][j + 1] += table[i][j]
                        f = True

                    if i < n - 2 and j > 0:
                        table[i + 2][j - 1] -= table[i][j]
                        f = True

        if not f:
            return table[n - 1][m - 1]


a, b = map(int, input().split())
table = [[0] * b for _ in range(a)]
table[0][0] = 1
print(F(a, b))

# Научите решать такое
