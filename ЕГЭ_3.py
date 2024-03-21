sp_0 = [x for x in open('ЕГЭ_3-1.txt')]
sp_2 = [int(x) for x in open('ЕГЭ_3-2.txt')]
sp_3 = [int(x) for x in open('ЕГЭ_3-3.txt')]

sp_1 = []
for elem in sp_1:
    if elem != 'NULL':
        sp_1.append(int(elem))

sp = []
count = 0
for i in range(len(sp_2)):
    if sp_2[i] in sp_1 and sp_3[i] > 1000000:
        sp.append(sp_2[i])

print(sp)

count = 0
for elem in sp_3:
    if elem > 1000000:
        count += 1

print(count)