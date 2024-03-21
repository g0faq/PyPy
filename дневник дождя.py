n, m = map(int, input().split())
a = 0
res = 0
if m > 7:
    res = m - 7
else:
    a = (14 - m) + n
    if a >= n + 7:
        res = n + 7
    else:
        res = m - (a - n)


print(res)