def F(n):
    m = [[0] * 11 for _ in range(11)]
    m[5] = [1] * 11
    p, d = 0, 2
    while d < 13:
        z = n
        while z % d == 0:
            t = m[0][p]
            i = 1
            while i < 11:
                m[i - 1][p] = m[i][p]
                i += 1
            m[10][p] = t
            z //= d
        p += 1
        d += 1

    return m


sp = [[64, 128], [9, 27], [64, 256], [125, 625], [36, 216], [7, 49], [64, 1024], [9, 81], [1000, 10000], [1, 11]]

for i in range(10 ** 100):
    f = False
    for elem in sp:
        if i % elem[0] == 0 and i % elem[1] != 0:
            f = True
        else:
            f = False
            break
    if f:
        print(i)