f = open('17_2024.txt')
sp = [int(x) for x in f]
m = 0
count = 0
ms = 0
for elem in sp:
    if str(abs(elem))[-2:] == '13' and elem > m:
        m = elem
for i in range(len(sp) - 3):
    x, y, z = len(str(abs(sp[i]))), len(str(abs(sp[i + 1]))), len(str(abs(sp[i + 2])))
    if (x == 3 and y == 3 and z != 3) or (x == 3 and y != 3 and z == 3) or (x != 3 and y == 3 and z == 3) and sp[i] + sp[i + 1] + sp[i + 2] <= m:
        count += 1
        if sp[i] + sp[i + 1] + sp[i + 2] > ms:
            ms = sp[i] + sp[i + 1] + sp[i + 2]

print(count, ms)