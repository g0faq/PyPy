n, m, k = map(int, input().split())
sp_k = []
for _ in range(k):
    sp_k.append(list(map(int, input().split())))

table_input = []
for _ in range(n):
    table_input.append(list(map(int, input().split())))

sp_k.sort()

min_t, max_t = [], []
f = False
for elem in sp_k:
    if not f:
        min_t = elem
        f = True
    else:
        max_t = elem

x = 0
y = 0

if k != 0:
    table_0 = [0] * max_t[0]
    for i in range(max_t[0]):
        table_0[i] = [0] * max_t[1]
    table_0[0][0] = table_input[0][0]

    for i in range(1, max_t[1]):
        table_0[0][i] = table_0[0][i - 1] + table_input[0][i]

    for i in range(1, max_t[0]):
        table_0[i][0] = table_0[i - 1][0] + table_input[i][0]

    for i in range(1, max_t[0]):
        for j in range(1, max_t[1]):
            a = table_input[i][j] + table_0[i - 1][j]
            b = table_input[i][j] + table_0[i][j - 1]
            table_0[i][j] = max(a, b)

    x = table_0[max_t[0] - 1][max_t[1] - 1] - 1
    y = max_t[0] + max_t[1] - 1

    n_1, m_1 = n, m
    n, m = n_1 - (min_t[0] - 1), m_1 - (min_t[1] - 1)
    table = [0] * n
    for i in range(n):
        table[i] = [0] * m
    table[0][0] = table_input[min_t[0] - 1][min_t[1] - 1]

    for i in range(1, m):
        table[0][i] = table[0][i - 1] + table_input[0][i]

    for i in range(1, n):
        table[i][0] = table[i - 1][0] + table_input[i][0]

    for i in range(1, n):
        for j in range(1, m):
            a = table_input[i][j] + table[i - 1][j]
            b = table_input[i][j] + table[i][j - 1]
            table[i][j] = max(a, b)

else:
    table = [0] * n
    for i in range(n):
        table[i] = [0] * m
    table[0][0] = table_input[0][0]

    for i in range(1, m):
        table[0][i] = table[0][i - 1] + table_input[0][i]

    for i in range(1, n):
        table[i][0] = table[i - 1][0] + table_input[i][0]

    for i in range(1, n):
        for j in range(1, m):
            a = table_input[i][j] + table[i - 1][j]
            b = table_input[i][j] + table[i][j - 1]
            table[i][j] = max(a, b)

print((table[n - 1][m - 1] + x) / ((n + m - 1) + y))
