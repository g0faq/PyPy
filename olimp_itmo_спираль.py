n = 15
s = 1
res = [0, 10 ** 10]
for a in range(1, n ** 2):
    s = a + 1
    for i in range(1, n // 2):
        if (n - i) * (4 * i) + 1 + a > n ** 2:
            s += ((n - i) * (4 * i) + 1 + a) - n ** 2
        else:
            s += ((n - i) * (4 * i) + 1 + a)
    if n % 2 != 0:
        if n ** 2 + a > n ** 2:
            s += (n ** 2 + a) - n ** 2
        else:
            s += n ** 2 + a
    x = 2
    for i in range(n // 2):
        if ((n - i) * x - (i * 2 + 1)) + a > n ** 2:
            s += (((n - i) * x - (i * 2 + 1)) + a) - n ** 2
        else:
            s += (((n - i) * x - (i * 2 + 1)) + a)
        x += 4
    if s < res[1]:
        res[1] = s
        res[0] = a

print(*res)
