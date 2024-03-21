f = open('26-k2.txt')
n, k = map(int, f.readline().split())
sp = [int(elem) for elem in f]
sp.sort()
sp = sp[k:][:-k]
res = [max(sp), 0]
for elem in sp:
    res[1] += elem
res[1] = res[1] // len(sp)
print(*res)