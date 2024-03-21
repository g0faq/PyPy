sp = [0] * 25
sp[20] = 1
for i in range(19, 2, -1):
    sp[i] += sp[i + 2]
    sp[i] += sp[i + 3]
    if i * 3 < 21:
        if i * 3 % 3 == 0:
            sp[i] += sp[i * 3]

print(sp)