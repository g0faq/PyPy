s = [int(x) for x in input().split()]
n, k = s[0], s[1]
sp = []
res = ''
for i in range(k):
    sp.append([int(x) for x in input().split()])
sp_2 = []
for elem in sp:
    for i in range(elem[0], elem[1] + 1):
        sp_2.append(i)
sp_2.sort()
sp_2 = set(sp_2)
for i in range(1, n + 1):
    if i in sp_2:
        res += '.'
    else:
        res += 'I'

print(res)