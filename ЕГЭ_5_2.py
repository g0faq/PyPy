res = []
for i in range(0, 1000):
    n = bin(i)[2:]
    if i % 3 == 0:
        n += n[-3:]
    else:
        n += bin((i % 3) * 3)[2:]
    s = int(n, 2)
    if s > 151:
        res.append(s)

print(min(res))