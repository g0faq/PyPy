f = open('27_B_11244.txt')
k = int(f.readline())
n = int(f.readline())
sp = [int(x) for x in f]

res = 0

for i in range(n - 1):
    for j in range(i + k, n, k):
        res = max(res, sp[i] * sp[j])

print(res)
