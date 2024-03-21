f = open('26.txt')
n = int(f.readline())
sp = [[int(x.split()[1]), int(x.split()[0])] for x in f]
sp.sort()
print(sp)

last = sp[0]
count = 1
for elem in sp:
    if (last[0] + 15) < elem[1]:
        count += 1
        last = elem
    if count == 17:
        break

for elem in sp:
    elem[0], elem[1] = elem[1], elem[0]
sp.sort()
res = sp[-1][0] - last[1]

print(last)
print(sp[-1])

count += 1

print(count, res)