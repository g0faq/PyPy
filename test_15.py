def task_15_1(sF, tf, m, p, q):
    result = 0

    p = [i for i in range(p[0], p[1] + 1)]
    q = [i for i in range(q[0], q[1] + 1)] if q else [-1]

    max_range = max(max(p) * 2, max(q) * 2)

    for a1 in range(1, max_range - 1):
        for a2 in range(a1 + result, max_range):
            a = [i for i in range(a1, a2)]
            f = True

            for x in range(1, max_range):

                F = int(eval(sF.lower()))
                if F != tf:
                    f = False
                    break

            if f:
                if m == 0:
                    return len(a)
                else:
                    result = max(result, len(a))

    return result


def task_15_2(sF, tf, m):
    result = 0
    count = 0

    max_range = 100
    for a in range(1, max_range):
        f = True

        for x in range(1, max_range):
            for y in range(1, max_range):

                F = int(eval(sF.lower()))
                if f == tf:
                    count += 1
                else:
                    f = False
                    break

        if f:
            if m == 0:
                return a
            else:
                result = max(result, a)

    return result if m == 0 else count


t = int(input("\033[1m\033[36m{}".format('Кол-во заданий: ')))
for _ in range(t):
    sf = input("\033[1m\033[33m{}".format('функция: '))
    tf = int(input("\033[1m\033[33m{}".format('ложь/истина: ')))
    m = int(input("\033[1m\033[33m{}".format('мин/макс: ')))
    type = int(input("\033[1m\033[33m{}".format('тип: ')))

    if type == 1:
        p = list(map(int, input("\033[1m\033[33m{}".format('Отрезок 1: ')).split()))
        q = list(map(int, input("\033[1m\033[33m{}".format('Отрезок 2: ')).split()))

        ans = f'Ответ: {task_15_1(sf, tf, m, p, q)}'
    else:
        ans = f'Ответ: {task_15_2(sf, tf, m)}'

    print("\033[1m\033[34m{}".format(ans))
    print("\033[1m\033[35m{}".format('-' * 10))
