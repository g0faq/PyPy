import sys

days = {'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',
        'воскресенье'}
dat = list(map(str.strip, sys.stdin))
sl = dict()
sp = []
for elem in dat:
    if elem.lower() in days or elem == '':
        continue
    words = elem.split(' ')
    cab = int(words[-1])
    sub = ' '.join(words[:-1])
    if cab in sl:
        subjects = sl[cab]
        if sub not in subjects:
            subjects.append(sub)
            sl[cab] = subjects
    else:
        sl[cab] = [sub]
cabs = list(sl.keys())
cabs.sort()
for cab in cabs:
    ss = ''
    for sub in sl[cab]:
        ss += ', ' + sub
    print(str(cab) + ':' + ss.strip(','))