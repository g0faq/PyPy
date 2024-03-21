sp = [[0] * 70 for _ in range(70)]
for s1 in range(69 * 2 + 1):
    for s2 in range(69 * 3 + 1):
        if sp[s1][s2] == 0:
            if s1 + s2 + 1 >= 69 or s1 * 2 + s2 >= 69 or s1 + s2 * 3 >= 69:
                sp[s1][s2] = 1
