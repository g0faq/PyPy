n = int(input())

sp = [1, 1] + [0] * (n * 2 + 2)
for i in range(2, n):
    sp[2 * i] = sp[i] + sp[i - 1]
    sp[2 * i + 1] = sp[i] - sp[i - 1]

print(sp)
print(sp[n])