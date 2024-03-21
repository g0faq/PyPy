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

    result = []

    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if look(sp[0], sp[i], sp[j]):
                matrix[i - 1][j - 1] = 1
                matrix[i - 1][n] += 1
                matrix[n][j - 1] += 1

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                if matrix[j][n] < matrix[n][j]:
                    if (i + 1) not in result:
                        result.append(i + 1)

    return result


t = int(input())
result = []
for _ in range(t):

    n = int(input())
    i_sp_tower = []
    for i in range(n):
        i_sp_tower.append(list(map(int, input().split())))

    ans = find_wrong(n, i_sp_tower)
    result.append([len(ans), ans])

for elem in result:
    print(elem[0])
    print(*elem[1])
