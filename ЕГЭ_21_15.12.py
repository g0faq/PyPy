sp = [0] * 102
sp[33] = 1

for i in range(33, 8, -1):
    sp[i] += sp[i + 1]
    sp[i] += sp[i * 3] + sp[i * 3 + 1] + sp[i * 3 + 2]

for i in range(10, 34):
    sp[i] = 0

for i in range(8, 0, -1):
    sp[i] += sp[i + 1]
    sp[i] += sp[i * 3] + sp[i * 3 + 1] + sp[i * 3 + 2]

print(sp[1])