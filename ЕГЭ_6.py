count = 0
for x in range(1, 8):
    for y in range(1, 8):
        if (y < x / 3 ** 0.5) or (y > -x / 3 ** 0.5 + 12):
            count += 1
print(count)