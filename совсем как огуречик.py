t = int(input())
sp_n = [abs(int(input())) for _ in range(t)]
res = []
for n in sp_n:
    res_count = 0
    while n != 0:
        count_s = 0
        a = n
        while a != 1:
            a //= 2
            count_s += 1
        k1 = count_s
        k2 = k1 + 1яччччччччччччччччччччччччч
        res_count += 1
        n = min((n - 2 ** k1), (2 ** k2 - n))
    res.append(res_count)

for elem in res:
    print(elem)