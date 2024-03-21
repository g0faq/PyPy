table = [[0] * 1000 for _ in range(1000)]

for s1 in range(80):
    for s2 in range(80):
        if s1 + s2 + 1 >= 79 or 3 * s1 + s2 >= 79 or s1 + 3 * s2 >= 79:
            table[s1][s2] = 1

res = []

for s1 in range(80):
    for s2 in range(80):
        if table[s1 * 3][s2] == 1:
            res.append(s1 + s2)


for s1 in range(79, 0, -1):
    for s2 in range(79, 0, -1):
        if table[s1][s2] == 0:
            res_m = [table[s1 + 1][s2], table[s1][s2 + 1], table[s1 * 3][s2], table[s1][s2 * 3]]
            res_ = [elem for elem in res_m if elem < 0]
            if res_:
                table[s1][s2] = -max(res_) + 1
            else:
                table[s1][s2] = -max(res_m)
