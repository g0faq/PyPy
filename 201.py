n = int(input())
sp = [1, 1]
for i in range(2, n + 1):
    sp.append(sp[i - 2] + sp[i - 1])
print(sp[n - 1])