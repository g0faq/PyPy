f = open('24_202310101.txt')
s = f.readline()
sp = s.split('A')

res = 0
for i in range(len(sp) - 1):
    x = sp[i] + 'A' + sp[i + 1]
    sp_2 = x.split('B')
    if x.count('B') != 0:
        for j in range(len(sp_2) - 1):
            y = sp_2[j] + 'B' + sp_2[j + 1]
            if y.count('A') == 1:
                res = max(res, len(y))


print(res)