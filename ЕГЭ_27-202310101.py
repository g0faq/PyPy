f = open('27-B.txt')
k = int(f.readline()) * 3
n = int(f.readline())
sp = [int(x) for x in f]

res = 0

for i in range(n - k - 1):
    for j in range(i + 1, n - k):
        a2 = sp[i + k + 1:]
        a3 = sp[:j - k]
        s = a2 + a3
        res = max(res, (sp[i] + sp[j] + max(s)))

print(res)