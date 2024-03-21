n = (49 ** 7 + 7 ** 21 - 7)
print(n)
sp = [x for x in str(n)]

res = ''
a = 1
while n != 0:
    res = str(n % 7) + res
    n /= 7
print(res)