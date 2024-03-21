def task_1():
    count, res = 0, 0
    for i in range(2894, 174832):
        s = str(i)
        su = 0
        if s[-1] == '8':
            for elem in s:
                su += int(elem)
            if su > 22:
                count += 1
        if count == 13:
            res = i

    return count, res


def task_2():
    count, res = 0, 0
    for i in range(1031, 125889):
        s = str(i)
        if s[-1] != 5 and (i ** 0.5) ** 2 == i:
            count += 1
            if res == 0 and s[-2:] == '36':
                res = i

    return count, res


def task_3():
    count, res = 0, 0
    for i in range(2848, 109500):
        s = str(i)
        su = 0
        if '9' in s:
            for elem in s:
                if int(elem) > 5:
                    su += int(elem)
            if su % 3 == 0:
                count += 1
                res = i
    return count, res


def task_4():
    count, res = 0, 0
    sp = []
    for i in range(1005, 147871):
        s = str(i)
        x = []
        for elem in s:
            x.append(int(elem))
        if '1' not in s:
            if max(x) - min(x) < 4:
                count += 1
                sp.append(i)
    res = sp[-25]

    return count, res


def task_5():
    count, res = 0, [0, 30000]
    for i in range(5903, 174204):
        sp = list(str(i))
        mn = set()
        dop_count = 0
        for elem in sp:
            mn.add(elem)
            if int(elem) > 3:
                dop_count += 1
        if dop_count == 3 and len(mn) == len(sp):
            count += 1
            if res[1] - res[0] > res[1] - i:
                res[0] = i

    return count, res[0]


def task_6():
    count, res = 0, 0
    for i in range(138, 603885):
        sp = list(str(i))
        mn = set()
        for elem in sp:
            mn.add(elem)
        if len(mn) != len(sp):
            x = 3
            while x < i:
                x **= 3
                if x == i:
                    count += 1
                    if sum(sp) > res:
                        res = i

    return count, res


def task_7():
    count, res = 0, 0
    for i in range(54123, 75321):
        dop_count = 0
        for j in range(10, 21):
            if i % j == 0:
                dop_count += 1
        if dop_count == 5:
            count += 1
            res = i

    return count, res


def task_8():
    count, res = 0, 0
    for i in range(1234567, 76543220):
        s = str(i)
        if (int(s[-2:]) - int(s[:2])) != 0:
            if i % (int(s[-2:]) - int(s[:2])):
                count += 1
                res = i

    return count, res


def task_9():
    count, res = 0, 0
    for i in range(12094, 7654322):
        s = hex(i)[2:]
        if s[-1] == 'F' and i % 3 == 0 and i % 8 != 0 and i % 14 != 0 and i % 19 != 0:
            count += 1
            res += i

    return res, count


def task_10():
    count, res = 0, 0
    for i in range(-5000, 5001):
        s = hex(i)[2:]
        if s[-1] == 'B' and i % 6 != 0 and i % 5 == 0 and i % 7 == 0:
            count += 1
            res = max(res, abs(i))

    return count, res


print(f'№1: {task_1()}')
print(f'№2: {task_2()}')
print(f'№3: {task_3()}')
print(f'№4: {task_4()}')
print(f'№5: {task_5()}')
print(f'№6: {task_6()}')
print(f'№7: {task_7()}')
print(f'№8: {task_8()}')
print(f'№9: {task_9()}')
print(f'№10: {task_10()}')