s = [int(e) for e in input().split()]
s.sort(reverse=True)
x, y, z, t = s[0], s[1], s[2], s[3]
a = t - y
b = x - a
c = y - b
print(a, b, c)
print(f'X: {a + b}')
print(f'Y: {c + b}')
print(f'Z: {a + c}')
print(f'T: {a + b + c}')
print('--------------------------------------------------')

a = t - y
b = t - z
c = t - x
print(a, b, c)
print(f'X: {a + b}')
print(f'Y: {c + b}')
print(f'Z: {a + c}')
print(f'T: {a + b + c}')