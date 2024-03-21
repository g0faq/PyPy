f = open('27B.txt')
n = int(f.readline())
k = int(f.readline())
sp = [int(x) for x in f]
sp_1 = []
for elem in sp:
    if elem % 157 == 0:
        sp_1.append(elem)

res = 10 ** 100
for elem in sp_1:
    i = sp.index(elem)
    if i - k >= 0 and i + k <= n:
        m1 = min(min(sp[:i - k]), min(sp[i + k + 1:]))
    elif i - k < 0:
        m1 = min(sp[i + k + 1:])
    elif i + k >= n:
        m1 = min(sp[:i - k])

    res = min(res, m1 * elem)

print(res)
