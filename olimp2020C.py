n = int(input())
sp = [0] * n
res = []

for i in range(n):
    sp[i] = [0] * n

for i in range(n):
    x = int(input())
    sp[i][x - 1] = 1

for i in range(n):
    for j in range(n):
        if sp[j][i] == 1:
            res.append(n - j)

for elem in res:
    print(elem)
