f = open('26-k3.txt')
n, k, m = map(int, f.readline().split())
sp = [int(elem) for elem in f]
sp.sort(reverse=True)
res = [sp[k - 1]]
sp = sp[k:]
res.append(sp[m - 1])
res[0], res[1] = res[1], res[0]
print(*res)