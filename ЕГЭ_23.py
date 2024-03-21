def list_of_trajectory(start_position, finish_position, trajectory):

    if start_position < finish_position:
        trajectory.sort()
        trajectory = [start_position] + trajectory + [finish_position]
    else:
        if not trajectory:
            return [start_position, finish_position]
        trajectory.sort(reverse=True)
        trajectory = [start_position] + trajectory + [finish_position]

    return trajectory


def result(list_of_actions, trajectory=None, not_trajectory=None, result=1):

    if not_trajectory is None:
        not_trajectory = []

    if trajectory is None:
        trajectory = []

    for i in range(len(trajectory) - 1):
        result = counter_ways(trajectory[i], trajectory[i + 1], list_of_actions, result, not_trajectory)
    return result


def counter_ways(start_position, finish_position, list_of_act, start_value=1, not_trajectory=None):

    if not_trajectory is None:
        not_trajectory = []

    LIST = [0] * (max(start_position, finish_position) * 20)
    LIST[start_position] = start_value

    x = -1 if start_position > finish_position else 1

    for i in range(start_position + x, finish_position + x, x):
        if str(i) not in not_trajectory:
            for symbol in list_of_act:
                if symbol[0] == '+':
                    LIST[i] += LIST[i - int(symbol[1:])]
                elif symbol[0] == '-':
                    LIST[i] += LIST[i + int(symbol[1:])]
                elif symbol == '*2+1':
                    LIST[i] += LIST[(i - 1) // 2]
                elif symbol[0] == '*':
                    if i % int(symbol[1:]) == 0:
                        LIST[i] += LIST[i // int(symbol[1:])]
                elif symbol[:2] == '//':
                    for j in range(int(symbol[2:])):
                        LIST[i] += LIST[i * int(symbol[2:]) + j]
                elif symbol[0] == '/':
                    LIST[i] += LIST[i * int(symbol[1:])]

    return LIST[finish_position]


def print_answer():
    answer = result(input_list_of_actions,
                    list_of_trajectory(input_start_position, input_finish_position, input_list_of_trajectories),
                    input_list_of_not_trajectories)

    print("\033[1m\033[31m{}".format('-' * 40))
    print("\033[1m\033[32m{}".format('ANSWER'), answer)


def Example_input():
    print("\033[1m\033[33m{}".format('EXAMPLE INPUT:'))
    print("\033[1m\033[34m{}".format('Start: '), "\033[1m\033[30m{}".format('1'))
    print("\033[1m\033[34m{}".format('Finish: '), "\033[1m\033[30m{}".format('10'))
    print("\033[1m\033[34m{}".format('Trajectory: '), "\033[1m\033[30m{}".format('2 8'))
    print("\033[1m\033[34m{}".format('Not in trajectory: '), "\033[1m\033[30m{}".format('5 7'))
    print("\033[1m\033[34m{}".format('Actions: '), "\033[1m\033[30m{}".format('+1'))

    print("\033[1m\033[31m{}".format('-' * 40))

    print("\033[1m\033[33m{}".format('ACTIONS:'))
    print("\033[1m\033[34m{}".format('Прибавить x: '), "\033[1m\033[30m{}".format('+x'))
    print("\033[1m\033[34m{}".format('Вычесть x: '), "\033[1m\033[30m{}".format('-x'))
    print("\033[1m\033[34m{}".format('Умножить на x: '), "\033[1m\033[30m{}".format('*x'))
    print("\033[1m\033[34m{}".format('Разделить на x: '), "\033[1m\033[30m{}".format('/x'))
    print("\033[1m\033[34m{}".format('Сделать нечетное из x: '), "\033[1m\033[30m{}".format('*2+1'))
    print("\033[1m\033[34m{}".format('Сделать четное из x: '), "\033[1m\033[30m{}".format('*2'))
    print("\033[1m\033[34m{}".format('Найти целую часть от деления на x: '), "\033[1m\033[30m{}".format('//x'))

    print("\033[1m\033[31m{}".format('-' * 40))


Example_input()

input_start_position = int(input("\033[1m\033[35m{}".format('Start: ')))
input_finish_position = int(input('Finish: '))
input_list_of_trajectories = list(map(int, input('Trajectory: ').split()))
input_list_of_not_trajectories = input('Not in trajectory: ').split()
input_list_of_actions = input('Actions: ').split()

print_answer()
