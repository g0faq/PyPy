a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
count = 0
for x in range(0, 1001):
    if x - e == 0:
        continue
    elif ((a * (x ** 3)) + (b * (x ** 2)) + (c * x) + d) / (x - e) == 0:
        count += 1
print(count)