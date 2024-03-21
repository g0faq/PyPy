def task_15_1(tf, m, P, Q):
    res = 0

    p = [i for i in range(P[0], P[1] + 1)]
    q = [i for i in range(Q[0], Q[1] + 1)]

    w = max(p[1] * 2, q[1] * 2)

    for a1 in range(1, w - 1):
        for a2 in range(a1 + 1, w):
            a = [i for i in range(a1, a2)]
            for x in range(1, 1000):

                F = not (x in p) or ((x in q) or not ((x in p) or not (x in a)))

                if int(F) != tf:
                    break

            else:
                if m == 1:
                    res = max(res, len(a))
                else:
                    return len(a)
    return res


def task_15_2(tf, m):
    res = 0

    for A in range(500):
        for x in range(1, 1000):
            for y in range(1, 1000):
                F = not (y + 2 * x <= 27) or ((y - x > 3) or (y <= A))
                if int(F) != tf:
                    break
        else:
            if m == 1:
                res = A
            else:
                return A

    return res


t = int(input('Кол-во заданий: '))
for _ in range(t):
    tf = int(input("\033[1m\033[33m{}".format('ложь/истина: ')))
    m = int(input("\033[1m\033[33m{}".format('мин/макс: ')))
    type = int(input("\033[1m\033[33m{}".format('тип: ')))

    if type == 1:
        p = list(map(int, input("\033[1m\033[33m{}".format('Отрезок 1: ')).split()))
        q = list(map(int, input("\033[1m\033[33m{}".format('Отрезок 2: ')).split()))

        ans = f'Ответ: {task_15_1(tf, m, p, q)}'
    else:
        ans = f'Ответ: {task_15_2(tf, m)}'

    print("\033[1m\033[34m{}".format(ans))
    print("\033[1m\033[35m{}".format('-' * 10))
