f = open('26-j8.txt')
sp = [int(x) for x in f]
n = sp[0]
del sp[0]

sp.sort()

count_1, count_2 = 0, 0
sp_max_1 = []
sp_max_2 = []

for i in range(n):
    if i < n * 0.7:
        count_1 += sp[i] * 0.7
        sp_max_1.append(sp[i] * 0.7)
    else:
        count_1 += sp[i] * 0.6
        sp_max_1.append(sp[i] * 0.6)

for i in range(n):
    if i < n * 0.5:
        count_2 += sp[i] * 0.6
        sp_max_2.append(sp[i] * 0.6)
    else:
        count_2 += sp[i] * 0.65
        sp_max_2.append(sp[i] * 0.65)

if count_1 > count_2:
    print(int(count_1 - count_2), int(max(sp_max_1)))
else:
    print(int(count_2 - count_1), int(max(sp_max_2)))