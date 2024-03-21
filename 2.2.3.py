res_count = 6
flag = False

for _ in range(111, 31111112):
    i = str(_)
    if '0' in str(i) or '9' in i or int(i) % 10 != int(i) % 100 // 10:
        flag = False
    else:
        flag = True
    if flag:
        sum_numbers = sum(map(int, i))
        if sum_numbers <= 10:
            res_count += 1
            print(f'Число: {i}        счётчик: {res_count}')

for _ in range(111111111, 211111112):
    i = str(_)
    if '0' in str(i) or '9' in i or int(i) % 10 != int(i) % 100 // 10:
        flag = False
    else:
        flag = True
    if flag:
        sum_numbers = sum(map(int, i))
        if sum_numbers <= 10:
            res_count += 1
            print(f'Число: {i}        счётчик: {res_count}')



print(res_count)