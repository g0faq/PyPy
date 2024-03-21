import math as m


def task_12_23(n):
    m = [[0] * 11 for _ in range(11)]
    m[5] = [1] * 11
    p, d = 0, 2
    while d < 13:
        z = n
        while z % d == 0:
            t = m[0][p]
            i = 1
            while i < 11:
                m[i - 1][p] = m[i][p]
                i += 1
            m[10][p] = t
            z //= d
        p += 1
        d += 1

    sp = [[64, 128], [9, 27], [64, 256], [125, 625], [36, 216], [7, 49], [64, 1024], [9, 81], [1000, 10000], [1, 11]]

    for i in range(10 ** 100):
        f = False
        for elem in sp:
            if i % elem[0] == 0 and i % elem[1] != 0:
                f = True
            else:
                f = False
                break
        if f:
            print(i)


def task_4_23():
    a = 961376769
    b = 1035574967097
    s = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    sp = list(s)
    sp.sort()
    s = ''.join(sp)

    x = 0
    while a % 3 == 0:
        x += 1
        a //= 3
    print(s[26 - x - 1])

    x = 0
    while b % 3 == 0:
        x += 1
        b //= 3
    print(s[26 - x - 1])


def task_5_23():
    for x in range(10000):
        n = x
        f = False
        m = [2, 3, 1]
        i, d = 0, 3
        while sum(m) != 0:
            if i > 2:
                print('ERROR')
                f = True
                break
            if m[i] != 0 and n % d == 0:
                n //= d
                m[i] -= 1
            else:
                d += 2
                i += 1
        if n == 1 and not f:
            print(x)
            break


def task_2_22():
    Iv = 208 * 8
    It = 144 * 8
    Ip = 12272 * 8 + Iv
    N = Ip / 5
    sp_m, sp_x = [], []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            sp_x.append(i)
            sp_m.append(N // i)

    sp_m.sort()
    sp_x.sort(reverse=True)

    for i in range(len(sp_x)):
        elem = [sp_m[i], sp_x[i]]
        if sp_m[i] % 16 == 0:
            n = sp_m[i] // 16
            if (m.log(int(n + 0.999), 2) + 5) * 16 == 144:
                print(sp_x[i])


def task_3_22():
    n16 = 'FEDCBA9876543210'
    n10 = int(n16, 16)
    n2 = bin(n10)[2:]
    # print(n16)
    # print(n10)
    # print(n2)
    sp = []
    for i in range(0, 64, 4):
        sp.append(n2[i:i + 4])

    res = ''

    for elem in sp:
        x0, x1, x2, x3 = elem[0], elem[1], elem[2], elem[3]
        F = int((x0 and x1 and x2) or (x1 and x2 and x3) or (x2 and x3 and x0))
        res = str(F) + res
        # print(hex(int(elem, 2))[2:], F)

    a = str(10 ** 10 * 6 ** 6)
    result = 0
    for elem in a:
        result += int(elem)
    print(result)

    # 1 - 10
    # 0 - 6

    # res = '0011' * 4 = 11001100110011
    # print(res)
    # print(int(res, 2))
    # print(2 ** 64)


def task_4_22(matrix):
    count = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == '.':
                x = [i, j]

                # fall
                for k in range(x[0], 9):
                    if matrix[k + 1][x[1]] == '.':
                        x = [k + 1, j]
                        if k == 8:
                            count += 1
                            break
                    else:
                        break

                # right
                for k in range(x[1], 9):
                    if matrix[x[0]][k + 1] == '.':
                        x = [x[0], k + 1]
                        if k == 8:
                            count += 1
                            break
                    else:
                        break

                # up
                for k in range(x[0], 0, -1):
                    if matrix[k - 1][x[1]] == '.':
                        x = [k - 1, x[1]]
                        if k == 1:
                            count += 1
                            break
                    else:
                        break

                # left
                for k in range(x[1], 0, -1):
                    if matrix[x[0]][k - 1] == '.':
                        x = [x[0], k - 1]
                        if k == 1:
                            count += 1
                            break
                    else:
                        break

                # up
                for k in range(x[0], 0, -1):
                    if matrix[k - 1][x[1]] == '.':
                        x = [k - 1, x[1]]
                        if k == 1:
                            count += 1
                            break
                    else:
                        break

    print(count)


matrix = [['*', '.', '*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
          ['*', '.', '*', '.', '*', '*', '.', '*', '.', '*'],
          ['*', '.', '*', '.', '.', '.', '.', '*', '.', '*'],
          ['*', '.', '*', '.', '*', '*', '.', '*', '.', '*'],
          ['*', '.', '*', '.', '*', '*', '.', '*', '.', '*'],
          ['*', '.', '*', '.', '.', '.', '.', '*', '.', '*'],
          ['*', '.', '*', '*', '*', '*', '*', '*', '.', '*'],
          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]


def task_5_22(rr):
    for n0 in range(10, 10 ** 10):
        print(n0)
        n = n0
        m = 8143989
        mas = [[0] * 8 for _ in range(8)]
        while m > 0:
            i = 0
            while i < 8:
                j = 0
                while j < 8:
                    if (i * j) % 8 == m % 8:
                        mas[i][j] = n % 8
                        j += 1
                i += 1
            n //= 8
            m //= 8

        if mas == rr:
            print(n0)
            break


right_res = [[5, 5, 5, 5, 5, 5, 5, 5],
             [5, 2, 3, 7, 4, 0, 1, 6],
             [5, 3, 4, 1, 5, 3, 4, 1],
             [5, 7, 1, 2, 4, 6, 3, 0],
             [5, 4, 5, 4, 5, 4, 5, 4],
             [5, 0, 3, 6, 4, 2, 1, 7],
             [5, 1, 4, 3, 5, 1, 4, 3],
             [5, 6, 1, 0, 4, 7, 3, 2]]


def task_16_23():
    t = [[0] * 101 for _ in range(101)]
    for i in range(100):
        t[i][0] = i + 1
        t[0][i] = i + 1

    res = 0
    for i0 in range(1, 101):
        for j0 in range(1, 101):
            table = t
            count = 0
            for i in range(1, i0):
                for j in range(1, j0):
                    table[i][j] = table[i - 1][j - 1] + min(table[0][j], table[i][0])
                    if table[i][j] == 79:
                        count += 1
            if count == 22:
                res += 1

    print(res)


def task_25_23():
    sp = []
    while True:
        try:
            s = input()
            if s != '':
                sp.append(s.split(','))
            else:
                break
        except EOFError:
            break
    sp_f = [1] * len(sp[0])

    for i in range(1, len(sp)):
        for j in range(len(sp[i])):
            if sp[i][j] != '':
                sp_f[j] = 0

    print(sum(sp_f))
    for i in range(len(sp_f)):
        if sp_f[i] == 1:
            print(sp[0][i])


def task_26_23():
    a, b, n, m = map(int, input().split())
    masks = [[] for _ in range(n)]
    res = [0] * n

    for i in range(n):
        s = ''
        for j in range(a):
            s += input()
        for j in range(a * b):
            if s[j] == '1':
                masks[i].append(j)

    for i in range(m):
        s = ''
        for _ in range(a):
            s += input()
        for j in range(n):
            f = True
            for e in masks[j]:
                if s[e] != '1':
                    f = False
                    break
            if f:
                res[j] += 1

    print(*res)


task_26_23()


def task_9_1(a, b, c, d, e):
    return int(a and (not b))


def task_9_2(a, b, c, d, e):
    return int(b and (not c))


def task_9_3(a, b, c, d, e):
    return int(c and (not d))


def task_9_4(a, b, c, d, e):
    return int(d and (not e))


def task_9_5(a, b, c, d, e):
    f1 = (not task_9_4(a, b, c, d, e)) or task_9_3(a, b, c, d, e)
    f2 = (not f1) or task_9_1(a, b, c, d, e)
    F = (not f2) or task_9_2(a, b, c, d, e)
    return int(F)


def task_9_23():
    n = '10111111000000001011111110111011'

    s = ''

    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                for d in (0, 1):
                    for e in (0, 1):
                        F = str(task_9_5(a, b, c, d, e))
                        s = F + s

    if s == n:
        print('YES')


def task_20_23():
    for d5 in range(1000):
        d4 = min(1343, 4 * d5 + 6 * 74 + 29)
        d3 = min(4043, 137 + 4 * 132 + 3 * d4 + 63)
        d7 = min(4124, 5 * 214 + 3 * 111 + 2 * d4 + 38)
        s = 2 * d3 + 3 * d7 + 160
        if s > 17953:
            print(d5 - 1)
            break


def task_22_23():
    f = open('23_23.txt')
    sp = [x[:-1] for x in f if x[0] == '1']

    sl = {}
    count = 0

    for elem in sp:
        if elem not in sl:
            if len(sl) == 4:
                maxx = [0, 0]
                for e in sl.keys():
                    if sl[e] > maxx[0]:
                        maxx[1] = e
                        maxx[0] = sl[e]
                del sl[maxx[1]]
            sl[elem] = 0
        else:
            sl[elem] = 0
            count += 1
        for key in sl.keys():
            sl[key] += 1

    print(count)


def task_27_23():

    f = open('input.txt')

    n = int(f.readline())
    sp = []
    sl = {}
    for _ in range(n):
        s = list(map(int, f.readline()[:-1].split()))[1:]
        sp.append(s)
        for elem in s:
            if elem not in sl:
                sl[elem] = [_]
            else:
                sl[elem].append(_)

    res = []
    m = int(f.readline())
    for i in range(m):
        s = f.readline()[:-1]
        a, b = s[0], int(s[1:])
        if a == '-':
            if b in sl:
                for elem in sl[b]:
                    del sp[elem][sp[elem].index(b)]
                del sl[b]
        else:
            res.append(len(sp[b - 1]))

    with open('output.txt', 'w') as f:
        for elem in res:
            f.write(f'{elem}\n')

