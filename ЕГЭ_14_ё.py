s = '0123456789ABCDEFGHIJKL'
for x in s:
    a = int(f'63{x}59685' + f'17{x}53' + f'36{x}5', 22)
    if a % 21 == 0:
        print(a // 21)