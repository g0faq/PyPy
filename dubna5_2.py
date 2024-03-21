def create_basket(goods, N, money):
    # на вход товары по возрастанию цены, кол-во товаров, кол-во денег
    # на выходе кол-во товаров В и остаток денег

    a_goods = list(filter(lambda x: x[1] == 'A', goods))
    b_goods = list(filter(lambda x: x[1] == 'B', goods))
    size, a_size, b_size, v_money = 0, 0, 0, money

    # определяем максимальное кол-во товаров, которое можем купить
    for g in goods:
        if v_money >= g[0]:
            size += 1
            v_money -= g[0]
        else:
            break

        # если можем купить все товары
        if size == N:
            return (len(b_goods), v_money)

    # заполняем корзину товарами B
    for g in b_goods:
        if money >= g[0]:
            b_size += 1
            money -= g[0]
        else:
            break

    # пока не достигнем нужного размера, добавляем товары А
    # удаляя самый дорогой товар В если закончились деньги
    while (b_size + a_size < size):
        if money >= a_goods[a_size][0]:
            money -= a_goods[a_size][0]
            a_size += 1
        else:
            b_size -= 1
            money += b_goods[b_size][0]
    return [b_size, money]


goods = []
with open('26 (1).txt') as f:
    N, M = map(int, f.readline().split())
    for line in f:
        a, b = line.split()
        goods.append([int(a), b])
    goods.sort(key=lambda x: x[0])

print(create_basket(goods, N, M))