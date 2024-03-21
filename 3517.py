
n = int(input())
if 10 < n < 20:
    print(f'{n} korov')
elif n % 10 == 1:
    print(f'{n} korova')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(f'{n} korovy')
else:
    print(f'{n} korov')