def T_51():
    sp = [0] * 5100
    sp[10] = 1

    for i in range(11, 52):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    for i in range(51):
        sp[i] = 0

    for i in range(51, 5100):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    return f'Траектория 51: {sp[5094]}'


def T(a, b):
    sp = [0] * 5100
    sp[10] = 1

    for i in range(11, a + 1):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    for i in range(a):
        sp[i] = 0

    for i in range(a, b + 1):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    for i in range(b):
        sp[i] = 0

    for i in range(b, 5100):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    for i in range(b, 52):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    for i in range(51):
        sp[i] = 0

    for i in range(51, 5100):
        sp[i] += sp[i - 1]
        if i * 2 % 3 == 0:
            sp[i] += sp[(i * 2) // 3]
        if (i * 2 + 1) % 3 == 0:
            sp[i] += sp[(i * 2 + 1) // 3]
        if i % 2 == 0:
            sp[i] += sp[i // 2]

    return f'Траектория {a}-{b}: {sp[5094]}'


print(T_51())
print(T(19, 33))
print(T(18, 35))
print(T(17, 31))