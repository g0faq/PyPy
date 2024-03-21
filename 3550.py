a, b, c, d = int(input()), int(input()), int(input()), int(input())
res = []
for i in range(a, b + 1):
    if i % d == c:
        res.append(i)
print(*res)