n, k = map(int, input().split())
sp = list(map(int, input().split()))
sp.sort(reverse=True)
res, m1, i = 0, sp[0], 1
if n > 1:
    m2 = sp[1]
    while i != k + 1:
        while m2 - 1 < m1:
            res += m1
            m1 -= 1
            i += 1
            if i == k + 1:
                break
        if i == k + 1:
            break
        m1 = sp[0]
else:
    while m1 != 0:
        res += m1
        m1 -= 1
print(res)