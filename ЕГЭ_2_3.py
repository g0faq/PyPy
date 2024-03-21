for i in range(10000, 0, -1):
    s = 127
    n = i
    while n - s > 0:
        s += 20
        n += 15
    if s == 627:
        print(i)
        break

