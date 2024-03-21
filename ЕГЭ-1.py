s = '0' + '1' * 18 + '2' * 11 + '3' * 7 + '0'
print(len(s))
while '00' not in s:
    s = s.replace('01', '210')
    s = s.replace('02', '3101')
    s = s.replace('03', '2012')

print(s)
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))

print('1: 1-1 1-2 0-3')
print('2: 2-1 1-2 1-3')
print('3: 3-3 3-2 1-1')

for i_1 in range(51):
    for i_2 in range(31):
        for i_3 in range(21):
            if i_1 * 1 + i_2 * 2 + i_3 * 3 == 61:
                if i_1 + i_2 + i_3 * 3 == 50:
                    if i_2 + i_3 == 18:
                        print(i_1, i_2, i_3)