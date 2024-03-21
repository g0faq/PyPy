def F(n):
    r, a, b, d, s = 0, 1, 1, 0, 0
    if '11' in bin(n)[2:]:
        return
    while n > 0:
        d = n % 2
        if d == 1:
            r += b
        if d + s < 2:
            n //= 2
            s = d
        t = a
        a = b
        b = t + b
    return r


i = 0
while F(i) != 259:
    i += 1
print(i)