listik = []
number_chek = 0
total = 0


def add_item(item_name, item_cost):
    global listik, total
    listik.append(f'{item_name} - {item_cost}')
    total += item_cost


def print_receipt():
    global number_chek, listik, total
    if len(listik) != 0:
        number_chek += 1
        print(f'Чек {number_chek}. Всего предметов: {len(listik)}')
        for elem in listik:
            print(elem)
        print(F'Итого: {total}')
        print('-----')
    total = 0
    listik = []