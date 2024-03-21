f = open('26-39.txt')
n, m = map(int, f.readline().split())
sp = [int(x) for x in f.read().split()]

count = 0
total = 0

sp.sort(reverse=True)
sp_2 = []
for elem in sp:
    if 310 <= elem <= 320 and total + elem <= m:
        count += 1
        total += elem
    else:
        sp_2.append(elem)


sp_3, sp_4 = [], []

sp_2 = sp_2[::-1]

for elem in sp_2:
    if elem + total <= m:
        total += elem
        count += 1
        sp_3.append(elem)
    else:
        sp_4.append(elem)

sp_2.sort(reverse=True)
sp_3.sort(reverse=True)
sp_4.sort(reverse=True)

for i in range(len(sp_3)):
    for j in range(len(sp_4)):
        if total - sp_3[i] + sp_4[j] <= m:
            total = total - sp_3[i] + sp_4[j]
            sp_3[i], sp_4[j] = sp_4[j], sp_3[i]

print(count, total)