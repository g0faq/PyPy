n, m = map(int, input().split())
sp = [[0] * m for _ in range(n)]

j = 1
for i in range(n):
    sp[i][j] = i * j

for elem in sp:
    print(*elem)
