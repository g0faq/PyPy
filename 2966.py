def T(n, m, t):

    letters_table = [[''] * m for _ in range(n)]

    table = [[0] * m for _ in range(n)]
    table[0][0] = t[0][0]

    for j in range(1, m):
        table[0][j] = table[0][j - 1] + t[0][j]
        letters_table[0][j] = letters_table[0][j - 1] + 'R '

    for i in range(1, n):
        table[i][0] = table[i - 1][0] + t[i][0]
        letters_table[i][0] = letters_table[i - 1][0] + 'D '

    for i in range(1, n):
        for j in range(1, m):
            if t[i][j] + table[i - 1][j] > t[i][j] + table[i][j - 1]:
                table[i][j] = t[i][j] + table[i - 1][j]
                letters_table[i][j] = letters_table[i - 1][j] + 'D '

            if t[i][j] + table[i][j - 1] > t[i][j] + table[i - 1][j]:
                table[i][j] = t[i][j] + table[i][j - 1]
                letters_table[i][j] = letters_table[i][j - 1] + 'R '

    return table[-1][-1], letters_table[-1][-1]


a, b = map(int, input().split())
tab = []
for i in range(a):
    tab.append(list(map(int, input().split())))

res = T(a, b, tab)
print(res[0])
print(res[1])
