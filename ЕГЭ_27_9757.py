sp = []
for i in range(1, int(2023 ** 0.5) + 1):
    if 2023 % i == 0:
        sp.append(2023 // i)
        sp.append(i)

sp.sort()
print(*sp)