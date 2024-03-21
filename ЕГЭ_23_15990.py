sp = [0] * 25
sp[2] = 1
for i in range(3, 12):
    sp[i] += sp[i - 2]
    sp[i] += sp[i - 3]
    if i % 2 == 0:
        sp[i] += sp[i // 2]
x = sp[11]
sp = [0] * 25
sp[11] = 1
for i in range(12, 23):
    sp[i] += sp[i - 2]
    sp[i] += sp[i - 3]
    if i % 2 == 0:
        sp[i] += sp[i // 2]


print(x * sp[22])