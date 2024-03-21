res = set()
for n in range (10, 1001):
    s = bin(n)[3:]
    res.add(n - int(s, 2))

print(len(res))