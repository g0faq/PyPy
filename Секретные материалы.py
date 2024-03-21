def print_document(pages):
    for elem in pages:
        if elem.split()[0] == 'Секретно':
            print('Дальнейшие материалы засекречены')
            return
        else:
            print(elem)
    print('Напечатано без купюр')
