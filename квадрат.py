n = int(input())
s = [[0] * n] * n

x = []
for i in range(1, n + 1):
    x.append(i)
s[0] = x

sp = []
for i in range(n+ 1, n * 2):
    sp.append(i)

x = []
for i in range(n - (n // 2), n + ((n + 1) // 2)):
    x.append(i + (n + 1))
s[n - 1] = x[::-1]

for elem in s:
    print(*elem)
