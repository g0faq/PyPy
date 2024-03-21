f = open('17_2024 (3).txt')
sp = [int(x) for x in f]
count = 0
n = len(sp)
ma = 0
res = 0
for elem in sp:
    if str(elem)[-2:] == '13':
        ma = max(ma, elem)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            elem1, elem2, elem3 = abs(sp[i]), abs(sp[j]), abs(sp[k])
            if (len(str(elem1)) == 3 and len(str(elem2)) == 3 and len(str(elem3)) != 3) or \
                    (len(str(elem1)) == 3 and len(str(elem2)) != 3 and len(str(elem3)) == 3) or \
                    (len(str(elem1)) != 3 and len(str(elem2)) == 3 and len(str(elem3)) == 3):
                if sp[i] + sp[j] + sp[k] <= ma:
                    count += 1
                    res = max(res, sp[i] + sp[j] + sp[k])


print(count, res)

