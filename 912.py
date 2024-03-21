def F(n):
    count = 0
    i = 0
    while i < 2 ** n:
        s = bin(i)[2:]
        if '111' not in s:
            count += 1
            i += 1
        i += 1
    return count


print(F(int(input())))