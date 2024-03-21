f = open('26-j10_test.txt')

d, c, n = map(int, f.readline().split())

sp = [int(x) for x in f]
sp.sort()
sp_2 = []

total_d, total_c = 0, 0
count = 0
max_d, max_c = 0, 0

for elem in sp:
    if elem + total_d <= d:
        total_d += elem
        count += 1
        max_d = elem
    else:
        sp_2.append(elem)

for elem in sp_2:
    if elem + total_c <= c:
        total_c += elem
        count += 1
        max_c = elem
