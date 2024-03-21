n = int(input())

sp = [0] * (n + 5)
sp[n] = 1
for i in range(n, -1, -1):
    sp[i] += sp[i + 1]
    sp[i] += sp[i + 2]
    sp[i] += sp[i + 3]

print(sp[0])