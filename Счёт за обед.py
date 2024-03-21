daily_food = []


def count_food(days):
    dop = 0
    for elem in days:
        dop += daily_food[elem]
    return dop
