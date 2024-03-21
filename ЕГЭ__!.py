res = 0
for i in range(1, 172):
    n = bin(i)[2:]
    if int(n) % 2 == 0:
        n += '10'
    else:
        n += '00'
    if int(n, 2) > 170:
        print(res)
        break
    else:
        res = i