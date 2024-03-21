count = 0
for i1 in range(10):
    for i2 in range(10):
        if int(f'829{i1}17{i2}') % 31 == 0:
            count += 1
        for j in range(10000):
            if int(f'{j}829{i1}17{i2}') % 31 == 0:
                count += 1
            if int(f'{j}829{i1}17{i2}') > 10 ** 9:
                break
print(count)

