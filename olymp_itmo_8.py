import time


def look(tower_0, tower_1, tower_2):
    if tower_0[1] > tower_1[1] and tower_1[1] <= tower_2[1]:
        return False

    if tower_0[1] < tower_1[1] and tower_1[1] >= tower_2[1]:
        return True

    if tower_1[1] == tower_0[1]:
        if tower_2[1] > tower_1[1]:
            return False

    elif tower_2[1] == tower_0[1]:
        if tower_1[1] < tower_2[1]:
            return False

    else:
        a_1 = abs((tower_1[0] - tower_0[0]) / (tower_1[1] - tower_0[1]))
        a_2 = abs((tower_2[0] - tower_0[0]) / (tower_2[1] - tower_0[1]))

        if tower_1[1] < tower_0[1]:
            if a_1 <= a_2:
                return False

        else:
            if a_1 >= a_2:
                return False

    return True


def find_wrong(n, sp):
    sp_towers = [i for i in range(2, n + 1)]
    sp_visible = []
    result = []

    sl = {}
    for i in range(1, n):
        sl[i] = [[0, 0], []]

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if look(sp[0], sp[i], sp[j]):
                sl[i][0][0] += 1
                sl[j][0][1] += 1
                sl[i][1].append(j)

    for i in range(1, n):
        count = 0
        for elem in sl[i][1]:
            count += sl[elem][0][0]
        if count <= sl[i][0][0]:
            for elem in sl[i][1]:
                if (elem + 1) not in result:
                    sp_visible.append(elem + 1)
        if sl[i][0] == [0, 0] and (i + 1) not in result:
            sp_visible.append(i + 1)

    for elem in sp_towers:
        if elem not in sp_visible:
            result.append(elem)

    return result


t = int(input())
result = []
for _ in range(t):

    n = int(input())
    i_x = input().split()
    i_y = input().split()
    i_sp_tower = []

    for i in range(n):
        i_sp_tower.append([int(i_x[i]), int(i_y[i])])

    ans = find_wrong(n, i_sp_tower)
    result.append([len(ans), ans])

for elem in result:
    print(elem[0])
    print(*elem[1])
