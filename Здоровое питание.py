def diet(foods):
    sp = foods.split(', ')
    c1 = 0
    c2 = 0
    for elem in sp:
        if elem in food['жирное'] or elem in food['сладкое'] or elem in food['мучное']:
            c1 += 1
        elif elem in food['диетическое']:
            c2 += 1
    if c1 > len(sp) / 2:
        return 'Не ешь столько, По!'
    else:
        return 'Так держать, Воин Дракона!'
