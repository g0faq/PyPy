def F(n, m, list_of_act, s=1, nt=0):

    sp = [0] * (max(n, m) * 10)
    sp[n] = s

    if n > m:
        for i in range(n, m - 1, -1):
            if i != nt:
                for elem in list_of_act:
                    if elem[0] == '-':
                        sp[i] += sp[i + int(elem[1:])]
                    if elem[0] == '/':
                        sp[i] += sp[i * int(elem[1:])]

    else:
        for i in range(n, m + 1):
            if i != nt:
                for elem in list_of_act:
                    if elem[0] == '+':
                        sp[i] += sp[i - int(elem[1:])]
                    if elem[0] == '*':
                        if i % int(elem[1:]) == 0:
                            sp[i] += sp[i // int(elem[1:])]

    return sp[m]


def counter(start, finish, list_of_actions, trajectory=0, not_trajectory=0):
    if not_trajectory == 0:
        if trajectory == 0:
            return F(start, finish, list_of_actions)
        else:
            return F(trajectory, finish, list_of_actions, F(start, trajectory, list_of_actions))

    else:
        if trajectory == 0:
            return F(start, finish, list_of_actions, 1, not_trajectory)
        else:

            if trajectory < not_trajectory:
                if start < finish:
                    return F(trajectory, finish, list_of_actions, F(start, trajectory, list_of_actions), not_trajectory)
                else:
                    return F(trajectory - 1, finish, list_of_actions, F(start, trajectory, list_of_actions),
                             not_trajectory)

            else:
                if start < finish:
                    return F(trajectory, finish, list_of_actions, F(start, trajectory, list_of_actions, 1,
                                                                    not_trajectory))
                else:
                    return F(trajectory - 1, finish, list_of_actions, F(start, trajectory, list_of_actions, 1,
                                                                        not_trajectory))


a = int(input('Start: '))
b = int(input('Finish: '))
c = int(input('Trajectory: '))
d = int(input('Not in trajectory: '))
e = input('Actions: ').split()
print(counter(a, b, e, c, d))
