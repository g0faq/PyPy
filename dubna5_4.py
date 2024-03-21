for i in range(5000):
    s = i
    n = 2
    while s * n <= 4096:
        s //= 2
        n *= 4
    if n == 2048:
        print(i)
        break
