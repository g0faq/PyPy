f = open('26-47.txt')

sp = [int(x) for x in f]
n = sp[0]
del sp[0]

res_count = 0
maxi = 0
for i in range(n - 1):
    count = 0
    print(i)
    for j in range(i + 1, n):
        for elem in sp:
            if (sp[i] + sp[j]) // 2 > elem:
                count += 1
        if count % 100 == 0:
            maxi = max(count, maxi)
            res_count += 1
        count = 0

print(res_count, maxi)