# task 10
print('Task 10')
for i in range(338472, 338494):
    res = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            res.append(j)
    if count == 4:
        res.append(i)
        print(*res)
print('-' * 20)

# task 11
print('Task 11')
for i in range(164700, 164752):
    res = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            res.append(j)
    if count == 6:
        res.append(i)
        print(*res)
print('-' * 20)

# task 24
print('Task 24')
for i in range(11275, 16328):
    res = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            res.append(j)
    if count == 5:
        res.append(i)
        print(*res)
print('-' * 20)

# task 25
print('Task 25')
for i in range(20789, 35672):
    res = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            res.append(j)
    if count == 5:
        res.append(i)
        print(*res)
print('-' * 20)

# task 32
print('Task 32')
count_m = 0
res = []
for i in range(394505, 394441 - 1, -1):
    sp = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            sp.append(j)
    sp.append(i)
    if count >= count_m:
        count_m = count
        res = sp
print(count_m, res[-1], res[-2])
print('-' * 20)

# task 33
print('Task 33')
count_m = 0
res = []
for i in range(286564, 287270):
    sp = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            sp.append(j)
    sp.append(i)
    if count >= count_m:
        count_m = count
        res = sp
print(count_m, res[-1], res[-2])
print('-' * 20)

# task 34
print('Task 34')
res = []
count_m = 0
for i in range(586132, 586430):
    sp = []
    count = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
            sp.append(j)
    sp.append(i)
    if count > count_m:
        res = []
        res.append(sp)
        count_m = count
    if count == count_m:
        res.append(sp)

print(count_m, res[0][-1], res[0][-2])
print(count_m, res[-1][-1], res[-1][-2])
print('-' * 20)

# task 91
print('Task 91')
s = 0
for i in range(4099, 26985):
    count = 0
    n = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
        if count == 1:
            n = i
        if count == 2:
            break
    if count == 1:
        for elem in str(n):
            s += int(elem)

print(s)
print('-' * 20)

# task 102
print('Task 102')
res_count = 0

print('-' * 20)