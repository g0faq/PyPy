count = 0
for i in range(2,  29, 3):
    count += 2 ** i

count += 2 ** 29 + (10 ** 8 - 571 - count)
print(count)

print(5 / 64 + (13 / 51))