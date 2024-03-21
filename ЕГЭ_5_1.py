for n in range(0, 97):
    x = bin(n)[2:]
    x += x[-1]
    if int(x) % 2 == 0:
        x += '00'
    else:
        x += '10'
    s = int(x, 2)
    if s > 97:
        print(n)
        break