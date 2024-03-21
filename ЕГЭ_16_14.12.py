def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n > 0 and n % 2 == 0:
        return F(n // 2)


count = 0
for i in range(1000000001):
    if bin(i)[2:].count('1') == 3:
        print(i)
        count += 1

print(count)