def production(fab, sp_res, energy):
    if sp_res[int(fab)][0] <= energy:
        return True
    return False


def creation(n, art, sp_art, count_res):
    count = 0
    for i in range(n):
        if sp_art[int(art) - 1][i] > count_res[i]:
            count += 1
    return count


def get_sl_acts(acts):
    sl_act = {}

    d = 0
    for elem in acts:
        x = elem.split()
        for i in range(d + 1, int(x[1])):
            sl_act[i] = 0
        if int(x[1]) not in sl_act:
            sl_act[int(x[1])] = []
            d = int(x[1])
        sl_act[int(x[1])].append(x[3] + ' ' + x[4])

    return sl_act


def actions(A, E, n, sp_res, sp_arts, sp_acts):

    sl_act = get_sl_acts(sp_acts)

    sp_prod = [1] * n
    count_res = [0] * n
    energy = A
    result = []

    for key in sl_act:
        flag = False

        energy += E
        for i in range(n):
            if sp_prod[i] == 1:
                if production(i, sp_res, energy):
                    count_res[i] += sp_res[i][1]
                    energy -= sp_res[i][0]

        if sl_act[key] != 0:
            for elem in sl_act[key]:

                elem_spl = elem.split()

                if elem_spl[1] == 'CREATE':
                    flag = True

                if elem_spl[1] == 'ON':
                    sp_prod[int(elem_spl[0]) - 1] = 1
                elif elem_spl[1] == 'OFF':
                    sp_prod[int(elem_spl[0]) - 1] = 0

        if sl_act[key] != 0:
            if flag:
                for elem in sl_act[key]:

                    elem_spl = elem.split()

                    if elem_spl[1] == 'CREATE':

                        ret_creat = creation(n, elem_spl[0], sp_arts, count_res)
                        if ret_creat == 0:
                            for i in range(n):
                                count_res[i] -= sp_arts[int(elem_spl[0]) - 1][i]
                            result.append('SUCCESS')
                        else:
                            result.append(f'FAILURE: deficient {ret_creat}')
    return result


t = int(input())
result = []
for _ in range(t):
    A, E, i_n = map(int, input().split())

    i_sp_res = []
    i_e = input().split()
    i_x = input().split()
    for i in range(i_n):
        i_sp_res.append([int(i_e[i]), int(i_x[i])])

    i_n_art = int(input())
    i_sp_art = [[0] * i_n for _ in range(i_n_art)]

    for i in range(i_n_art):
        i_k = int(input())
        for j in range(i_k):
            i_rfa = input().split()
            i_sp_art[i][int(i_rfa[0]) - 1] = int(i_rfa[1])

    i_n_act = int(input())
    i_sp_act = []
    for _ in range(i_n_act):
        i_sp_act.append(input())

    result.append(actions(A, E, i_n, i_sp_res, i_sp_art, i_sp_act))

for elem_1 in result:
    for elem_2 in elem_1:
        print(elem_2)
