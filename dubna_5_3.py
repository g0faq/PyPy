f = open('27_B123.txt')
n = f.readline()
sp = [list(map(int, x.split())) for x in f]

for i in range(len(sp)):
    x, y = sp[i][0], sp[i][1]
    sp[i][0], sp[i][1] = min(x, y), max(x, y)

sp.sort(reverse=True)
su = 0

for elem in sp:
    su += elem[1]

a = 10 ** 20
for elem in sp:
    if elem[1] - elem[0] < a and elem[1] != elem[0] and (elem[1] - elem[0]) % 33 != 0:
        a = sp.index(elem)

su -= sp[a][1] + sp[a][0]

print(su)
print(su % 33)