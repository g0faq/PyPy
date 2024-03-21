def F(k, a, b):
    for n in range(60):
        i = 0
        for j in range(n, -1, -1):
            table[i][j] = k
            if i == a and j == b:
                print(1000 - table[i][j] + 1)
                return
            i += 1
            k += 1


table = [[0] * 60 for _ in range(60)]
F(1, 9, 30)