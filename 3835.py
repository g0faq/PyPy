s = [int(x) for x in input().split()]
m = 1001
for elem in s:
    if elem > 0 and elem < m:
        m = elem
print(m)