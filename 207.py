def F(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = b, a + b
    return b


print(F(int(input())))