s = []


def hello(name):
    global query, s
    if 'None' in query:
        print(f'Простите, {name}. Все окна заняты')
    else:
        for i in range(len(query)):
            if str(query[i]) == 'None':
                print(f'Здравствуйте, {name}! Подойдите к окошку номер {i + 1}')
                s.append(name)
                query[i] = name
                break


def search_card(name):
    if name not in s:
        print(f'Простите, {name}, дождитесь своей очереди')
    elif name in base:
        print(f'Ваша карта с номером {base.index(name) + 1} найдена')
    else:
        print('Ваша карта не найдена')


def good_bye(name):
    query[query.index(name)] = None
    print(f'До свидания, не болейте, {name}')


base = ["Елена Боброва", "Иван Протопопов", "Дмитрий Воротынский", "Роман Зулейко", "Кирилл Картошкин"]
query = [None, None]

hello("Елена Боброва")
hello("Иван Протопопов")
search_card("Елена Боброва")
hello("Кирилл Картошкин")
search_card("Кирилл Картошкин")