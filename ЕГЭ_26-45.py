f = open('26-45.txt')
sp = [int(x) for x in f]
n = sp[0]
del sp[0]

count, res = 0, 0

for i in range(n - 1):
    print(f'{i}/{5000}')
    for j in range(i + 1, n):
        if (sp[i] + sp[j]) % 2 == 0 and (sp[i] + sp[j]) // 2 in sp:
            count += 1
            res = max(res, (sp[i] + sp[j]) // 2)

print(count, res)

# 331 98715310