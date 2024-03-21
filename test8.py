sl = {'saturday': [], 'monday': []}
s = ''
while True:
    s = input()
    if s == '0':
        break
    if s.split()[0] == '1':
        sl['saturday'].append(s.split()[1])
    else:
        sl['monday'].append(s.split()[1])


print('Суббота')
for elem in sl['saturday']:
    print(elem)
print(len(sl['saturday']))
print('-' * 25)
print('Понедельник')
for elem in sl['monday']:
    print(elem)
print(len(sl['monday']))