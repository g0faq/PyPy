s = [int(x) for x in input().split()]
s.insert(0, -10000000000000000000000000000)
s.append(100000000000000000000000000000000)
c = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i - 1] and s[i] > s[i + 1]:
        c += 1
print(c)