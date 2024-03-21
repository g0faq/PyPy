s = 'abccba'
while len(s) != 80808021:
    s = s.replace('cc', 'bcacb', s.count('cc'))
    s = s.replace('bb', 'acbca', s.count('bb'))
    s = s.replace('aa', 'cbabc', s.count('aa'))
    print(len(s))
    print(s.count('a'))
    print(s.count('b'))
    print(s.count('c'))
    print('-')

print(s.count('a'), s.count('b'), s.count('c'))


a, b, c, x = 5, 6, 10, 21
while x != 80808021:
    a += 8
    b += 4
    c += 12
    x += 24

print(26936005, )