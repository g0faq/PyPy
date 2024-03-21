def possible_turns(cell):
    s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    x, y = s.index(cell[0]), int(cell[1])
    up1 = (x + 1, y + 2)
    up2 = (x - 1, y + 2)
    down1 = (x + 1, y - 2)
    down2 = (x - 1, y - 2)
    right1 = (x + 2, y + 1)
    right2 = (x + 2, y - 1)
    left1 = (x - 2, y + 1)
    left2 = (x - 2, y - 1)
    sp = [up1, up2, down1, down2, right1, right2, left1, left2]
    v = []
    for elem in sp:
        a = ''
        if -1 < elem[0] < 8 and 0 < elem[1] < 9:
            a = s[elem[0]] + str(elem[1])
            v.append(a)
    v.sort()
    return v