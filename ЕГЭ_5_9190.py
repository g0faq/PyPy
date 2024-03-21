count = 0
for i in range(100, 1000):
    x = str(i)
    a, b = int(x[0]) + int(x[1]), int(x[1]) + int(x[2])
    if str(a) + str(b) == '1216' or str(b) + str(a) == '1216':
        count += 1

print(count)
print(int('100011', 3))