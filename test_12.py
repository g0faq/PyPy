def task_15(tf, m, P, Q):
    res = 0

    x = 1
    a = [1, 2]
    p = [i for i in range(P[0], P[1] + 1)]
    q = [i for i in range(Q[0], Q[1] + 1)]

    for a1 in range(1, 99):
        for a2 in range(a1 + 1, 100):
            a = [i for i in range(a1, a2)]

            f = True

            for x in range(1, 1000):

                F = not ((x in a) and (x not in q)) or (not (x not in p) or (x in q))

                if int(F) != tf:
                    f = False
                    break

            if f:
                if m == 1:
                    res = max(res, len(a))
                else:
                    return len(a)

    return res


t = int(input('Кол-во заданий: '))
for _ in range(t):
    tf = int(input('Найти ложь/истина: '))
    m = int(input('Найти мин/макс длину: '))
    p = list(map(int, input('Отрезок 1: ').split()))
    q = list(map(int, input('Отрезок 2: ').split()))

    ans = f'Ответ: {task_15(tf, m, p, q)}'

    print(ans)
    print('-' * 10)