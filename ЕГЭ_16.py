'''def F(n):
    if n == 1:
        return 1
    else:
        return F(n - 1) + n

print(F(40))'''

def F(n):
    if n == 1:
        return 3
    return 2 * F(n - 1) - n + 1

print(F(21))