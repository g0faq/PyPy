count = 0
for i in range(10):
    if int(f'{i}1231') % 11 == 0:
        count += 1
    for j in range(10000):
        if int(f'{i}123{j}1') > 10 ** 7:
            break
        if int(f'{i}123{j}1') % 11 == 0:
            count += 1
print(count)