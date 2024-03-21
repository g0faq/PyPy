res_count = 5
flag = False
for _ in range(111, 1111111112):
    i = str(_)
    if '0' in str(i) or '9' in i or int(i) % 10 != int(i) % 100 // 10:
        flag = False
    else:
        flag = True
    if int(i) > 2111111111:
        res_count += 1
        break
    if flag:
        sum_numbers = sum(map(int, i))
        if sum_numbers <= 10:
            res_count += 1
            print(f'Число: {i}        счётчик: {res_count}')

print(res_count)