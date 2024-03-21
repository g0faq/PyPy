def task_19():
    for s in range(113):
        if table[3][s] == 0 and (table[6][s] == 1 or table[3][s * 2] == 1):
            return s


def task_20():
    ...


def task_21():
    ...


table = [[0] * 240 for _ in range(240)]

for s1 in range(113):
    for s2 in range(113):
        if s1 * 2 + s2 >= 118 or s1 + s2 * 2 >= 118:
            table[s1][s2] = 1
