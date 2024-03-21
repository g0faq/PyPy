for n in range(3, 10000):
    s = '5' + '2' * n
    while s.count('52') != 0 and s.count('2222') != 0 or s.count('1122') != 0:
        if s.count('52') != 0:
            s = s.replace('52', '11')
        if s.count('2222') != 0:
            s = s.replace('2222', '5')
        if s.count('1122') != 0:
            s = s.replace('1122', '5')
    su = 0
    for elem in s:
        su += int(elem)
    if su == 64:
        res = n

print(res)