n = int(input())
res = []
for i in range(int('9' * n), 10 ** (n - 1) - 1, -1):
    if i % 2 != 0:
        res.append(i)
print(*res)