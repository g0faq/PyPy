for i in range(10):
    print("\033[34m{}".format(i + 1))
    n, k, m, a = int(input()), int(input()), int(input()), int(input())
    count_hours = 0
    count_day = 0
    i = 1
    while count_hours < a:
        if i != n:
            count_hours += k
            count_day += 1
            i += 1
        else:
            count_hours += m
            count_day += 1
            i = 1

    res = count_day % n
    if res != 0:
        print(res)
    else:
        print(n)
    print('-' * 10)
