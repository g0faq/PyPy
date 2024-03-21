s = '0123456789ABCD'
for x in s:
    a = int('1' + x + '563', 14) + int('871' + x + '3', 14)
    if a % 24 == 0:
        print(a // 24)