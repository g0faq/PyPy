import math

print('-' * 29)

# task 3
k = [12, 16, 18, 23, 35, 33, 24, 17, 14, 26]
n = [100, 90, 80, 88, 80, 64, 40, 32, 20, 80]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(k[i])) * n[i]) / 8))

print('Task 3')
print(*res)
print('-' * 29)

# task 4
k = [612, 165, 280, 45, 1050, 35, 720, 103, 154, 260]
n = [120, 70, 80, 88, 80, 64, 40, 32, 20, 80]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(k[i])) * n[i]) / 8))

print('Task 4')
print(*res)
print('-' * 29)

# task 5
k = [0, 0, 0, 1, 10, -100, -20, -40, -50, -273]
l = [25, 50, 100, 200, 500, 100, 20, 40, 50, 100]
n = [70, 100, 120, 75, 80, 100, 80, 88, 80, 160]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(abs(l[i] - k[i]))) * n[i]) / 8))

print('Task 5')
print(*res)
print('-' * 29)

# task 6
k = [8, 15, 18, 20, 35, 6, 32, 14, 12, 24]
n = [80, 100, 120, 88, 80, 160, 72, 128, 80, 160]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(k[i])) * n[i]) / 8))

print('Task 6')
print(*res)
print('-' * 29)

# task 7
m = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
n = [100, 90, 80, 70, 60, 70, 80, 90, 100, 90]
res = []
for i in range(10):
    res.append((3 + m[i]) * n[i])

print('Task 7')
print(*res)
print('-' * 29)

# task 8
m = [12, 15, 10, 25, 8, 32, 28, 16, 18, 14]
n = [100, 80, 60, 40, 50, 30, 40, 60, 70, 55]
res = []
for i in range(10):
    res.append((5 + m[i]) * n[i])

print('Task 8')
print(*res)
print('-' * 29)

# task 9
m = [16, 12, 13, 17, 18, 22, 26, 10, 11, 14]
n = [100, 80, 60, 40, 50, 70, 90, 100, 80, 70]
res = []
for i in range(10):
    res.append((3 + 3 + m[i]) * n[i])

print('Task 9')
print(*res)
print('-' * 29)

# task 10
k = [5, 6, 7, 8, 5, 6, 7, 8, 5, 6]
m = [32, 26, 21, 20, 18, 6, 12, 17, 22, 28]
n = [100, 90, 60, 40, 55, 70, 85, 100, 80, 70]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(m[i] + 10)) * k[i]) / 8) * n[i])

print('Task 10')
print(*res)
print('-' * 29)

# task 11
k = [6, 7, 8, 6, 7, 8, 3, 7, 8, 9]
m = [3, 3, 3, 4, 4, 4, 2, 4, 5, 6]
n = [16, 26, 36, 42, 53, 64, 72, 68, 32, 54]
res = []
for i in range(10):
    res.append(math.ceil((m[i] * 5 + (k[i] - m[i]) * 4) / 8) * n[i])

print('Task 11')
print(*res)
print('-' * 29)

# task 12
k = [8, 9, 10, 11, 12, 13, 8, 9, 10, 11]
m = [26, 20, 22, 32, 34, 24, 18, 25, 16, 24]
s = [3, 6, 9, 12, 3, 6, 9, 12, 15, 17]
n = [16, 6, 36, 42, 53, 64, 72, 68, 32, 54]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log2(2 * m[i] + s[i] + 10)) * k[i]) / 8) * n[i])

print('Task 12')
print(*res)
print('-' * 29)

# task 13
k = [8, 9, 10, 11, 12, 13, 8, 9, 10, 11]
m = [16, 10, 8, 12, 14, 20, 18, 21, 26, 24]
l = [10, 12, 15, 21, 6, 9, 25, 14, 17, 22]
n = [35, 25, 15, 42, 33, 62, 78, 87, 23, 18]
res = []
for i in range(10):
    res.append(math.ceil(((math.ceil(math.log2(2 * m[i] + 10)) * k[i]) / 8) + l[i]) * n[i])

print('Task 13')
print(*res)
print('-' * 29)

# task 14
k = [9, 8, 7, 9, 8, 7, 9, 8, 7, 10]
m = [10, 12, 20, 26, 24, 22, 16, 14, 12, 8]
n = [30, 23, 46, 12, 17, 19, 27, 46, 38, 40]
s = [600, 368, 782, 120, 255, 456, 594, 828, 912, 1120]
res = []
for i in range(10):
    res.append(s[i] - math.ceil((math.ceil(k[i] * math.ceil(math.log2(m[i] * 2 + 10))) / 8) * n[i]))

print('Task 14')
print(*res)
print('-' * 29)

# task 17
p = [25, 30, 35, 40, 70, 80, 150, 200, 300, 1000]
k = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
m = [5, 6, 7, 8, 14, 12, 1, 8, 6, 4]
n = [26, 20, 15, 3, 2, 2, 15, 10, 8, 5]
res = []
for i in range(10):
    res.append(math.ceil((math.ceil(math.log(p[i], 2) + k[i])) / 8) + math.ceil(
        (math.ceil(m[i] * math.log((2 * n[i] + 10), 2))) / 8))

print('Task 17')
print(*res)
print('-' * 29)

# task 18
p = [1800, 700, 600, 500, 300, 200, 100, 80, 50, 20]
m = [11, 10, 9, 8, 7, 6, 5, 6, 7, 8]
n = [10, 15, 20, 22, 26, 15, 10, 20, 18, 16]
s = [21, 28, 18, 16, 31, 11, 14, 13, 16, 17]
res = []
for i in range(10):
    res.append(8 * s[i] - m[i] * math.ceil(math.log(2 * n[i], 2)) - math.ceil(math.log(p[i], 2)))

print('Task 18')
print(*res)
print('-' * 29)

# task 19
k = [15, 11, 7, 8, 5, 3, 22, 17, 19, 9]
m = [8, 9, 10, 11, 12, 11, 10, 9, 8, 7]
n = [15, 18, 20, 12, 6, 26, 14, 10, 18, 21]
d = [8, 9, 10, 9, 8, 9, 10, 9, 8, 11]
res = []
for i in range(10):
    res.append(k[i] + math.ceil((m[i] * math.ceil(math.log((2 * n[i] - 10), 2))) / 8) + math.ceil(
        (5 * math.ceil(math.log(26, 2))) + (d[i] - 5) * math.ceil(math.log(10, 2)) / 8))

print('Task 19')
print(*res)
print('-' * 29)
