def M(n):
    s = 0
    count = 0
    for items in range(n // 2 + 1, 1, -1):
        if n % items == 0:
            if items > 10000:
                return 0
            s += items
            count += 1
            if count == 2:
                return s
    return 0


res = []
i = 11000000
while len(res) != 5:
    m = M(i)
    if 0 < m < 10000:
        res.append(str(m))
    i += 1
    print(i, *res)

print('*'.join(res))
