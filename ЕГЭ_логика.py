def F(a, b, c):
    return ((a and (not c)) or ((not b) and (not c)))

print('a b c F')

for b in (0, 1):
    for a in (0, 1):
        for c in (0, 1):
            if (a and (not c)) or ((not b) and (not c)):
                print(a, b, c, 1)
            else:
                print(a, b, c, 0)