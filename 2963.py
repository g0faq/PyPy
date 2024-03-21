def F(n):
    s = ''
    while n != 1:
        if n % 3 == 0:
            s += '3'
            n //= 3
        elif (n - 1) % 3 == 0:
            n -= 1
            n //= 3
            s += '13'
        elif n % 2 == 0:
            s += '2'
            n //= 2
        else:
            s += '1'
            n -= 1
    return len(s)


print(F(32718))