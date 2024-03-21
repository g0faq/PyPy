def fac_1(n):
    if n == 0: return 1
    else: return n * fac_1(n - 1)


def fac_2(n):
    res = 1
    if n == 0: return 1
    else:
        for i in range(1, n + 1):
            res *= i
    return res


print(fac_1(4))
print(fac_2(4))