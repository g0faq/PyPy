m = '3?6906*4'
res = []


def F(x, y):
    if y == '':
        return int(f'3{x}69064')
    return int(f'3{x}6906{y}4')


for i in range(10):
    if F(i, '') % 2024 == 0:
        res.append(F(i, ''))
    for j in range(10000):
        a = F(i, str(j))
        if a > (10 ** 10):
            break
        if a % 2024 == 0:
            res.append(a)

for i in range(10):
    for j in range(10):
        a = F(i, ('00' + str(j)))
        if a > (10 ** 10):
            break
        if a % 2024 == 0:
            res.append(a)

for i in range(10):
    for j in range(100):
        if i == 8 and j == 18:
            print(F(i, ('0' + str(j))))
        a = F(i, ('0' + str(j)))
        if a > (10 ** 10):
            break
        if a % 2024 == 0:
            res.append(a)

res.sort()

for i in range(len(res)):
    res[i] = str(res[i])

print('*'.join(res))