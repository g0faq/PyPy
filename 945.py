def F(n, m):
    if m == 8:
        return 1
    sp = [[0] * 8 for i in range(8)]
    sp[9 - m - 1][n - 1] = 1
    for i in range(8 - m, 0, -1):
        for j in range(8):
            if sp[i][j] != 0:
                if j != 0:
                    sp[i - 1][j - 1] += sp[i][j]
                if j != 7:
                    sp[i - 1][j + 1] += sp[i][j]
    return sum(sp[0])


a, b = map(int, input().split())
print(F(a, b))