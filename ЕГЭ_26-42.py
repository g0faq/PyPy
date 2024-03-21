f = open('26-42.txt')
n, s = map(int, f.readline().split())
sp_0 = [x.split() for x in f]
sp, sl = [], {}

x = 0

for elem in sp_0:
    if elem[0] == 'A':
        sp.append(int(elem[1]))
        sl[int(elem[1])] = int(elem[2])
    else:
        x += int(elem[1]) * int(elem[2])

sp.sort()
a = 0
count = 0

for elem in sp:
    if sl[elem] * elem + x <= s:
        x += sl[elem] * elem
        count += sl[elem]
    else:
        a = elem
        break

while True:
    if x + a <= s:
        x += a
        count += 1
    else:
        break

print(count, s - x)