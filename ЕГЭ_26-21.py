f = open('26-k1.txt')
n, k = map(int, f.readline().split())
sp = [int(elem) for elem in f]
sp.sort()
res = [sp[-k - 1], 0]
sp.sort(reverse=True)
for i in range(k):
    res[1] += int(sp[i] * 0.2)
print(*res)