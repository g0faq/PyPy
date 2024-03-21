f = open('26-j10.txt')
d, c, n = map(int, f.readline().split())
sp = [int(x) for x in f]

sp.sort()

sp_d, sp_c = [], []
for elem in sp:
    if elem >= 500:
        sp_d.append(elem)
    else:
        sp_c.append(elem)


def F(sp_1, m):
    sp_1.sort()
    sp_2, sp_3 = [], []
    count = 0
    total = 0

    for elem in sp_1:
        if elem + total <= m:
            total += elem
            count += 1
            sp_2.append(elem)
        else:
            sp_3.append(elem)

    sp_1, sp_2, sp_3 = sp_1[::-1], sp_2[::-1], sp_3[::-1]

    if sum(sp_2) - max(sp_2) + max(sp_3) <= m:
        return [count, max(sp_3)]


print(F(sp_d, d)[0] + F(sp_c, c)[0], F(sp_d, d)[1] + F(sp_c, c)[1])