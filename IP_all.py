def bin_of_ip(mask):
    parts_of_mask = mask.split('.')  # делим маску на байты
    bin_mask = ''
    for elem in parts_of_mask:  # складываем все байты маски
        bin_of_part = bin(int(elem))[2:]
        bin_mask += '0' * (8 - len(bin_of_part)) + bin_of_part  # добавление 0 для полной записи
    return bin_mask


def number_of_PC(bin_mask, bin_ip):
    for i in range(32):
        if bin_mask[i] == '0':
            return f'Номер компьютера: {int(bin_ip[i:], 2)}'


def min_third_byte_of_mask(ip, ip_net, list_ips):
    for elem in list_ips:
        if int(ip.split('.')[2]) & elem == int(ip_net.split('.')[2]):
            return elem


def min_fourth_byte_of_mask(ip, ip_net, list_ips):
    for elem in list_ips:
        if int(ip.split('.')[3]) & elem == int(ip_net.split('.')[3]):
            return f'Минимальное значение третьего байта: {elem}'


def min_1(ip_node, ip_net, list_ips):
    if ip_node.split('.')[0] == ip_net.split('.')[0] and ip_node.split('.')[1] == ip_net.split('.')[1] and\
            ip_node.split('.')[3] == '0' or ip_net.split('.')[3] == '0':
        for elem in list_ips:
            if int(ip_node.split('.')[2]) & elem == int(ip_net.split('.')[2]):
                return 16 + bin(elem)[2].count('1')
    elif ip_node.split('.')[0] == ip_net.split('.')[0] and ip_node.split('.')[1] == ip_net.split('.')[1] and \
            ip_node.split('.')[2] == ip_net.split('.')[2]:
        for elem in list_ips:
            if int(ip_node.split('.')[3]) & elem == int(ip_net.split('.')[3]):
                return 32 + bin(elem)[2].count('1')
    if ip_node.split('.')[0] == ip_net.split('.')[0] and ip_node.split('.')[1] == ip_net.split('.')[1] and \
            ip_node.split('.')[2] == '0' or ip_net.split('.')[2] == '0':
        for elem in list_ips:
            if int(ip_node.split('.')[3]) & elem == int(ip_net.split('.')[3]):
                return 32 + bin(elem)[2].count('1')


def max_third_byte_of_mask(ip, ip_net, list_ips):
    for elem in list_ips:
        if int(ip.split('.')[2]) & elem == int(ip_net.split('.')[2]) & elem:
            return elem


def max_fourth_byte_of_mask(ip, ip_net, list_ips):
    for elem in list_ips:
        if int(ip.split('.')[3]) & elem == int(ip_net.split('.')[3]) & elem:
            return elem


def count_mask(ip_node, ip_net, list_ips):
    count = 0
    parts_node = ip_node.split('.')
    parts_net = ip_net.split('.')
    for elem in list_ips:
        if int(parts_node[2]) & elem == int(parts_net[2]):
            count += 1
    for elem in list_ips:
        if int(parts_node[3]) & elem == int(parts_net[3]):
            count += 1
    return count


def sum_of_1(ip, mask):
    count = 0
    parts_mask = mask.split('.')
    parts_ip = ip.split('.')
    for i in range(256):
        if i & int(parts_mask[3]) == int(parts_ip[3]):
            count_1 = bin(parts_ip[0])[2:].count('1') + \
                      bin(parts_ip[1])[2:].count('1') + \
                      bin(parts_ip[2])[2:].count('1') + \
                      bin(i)[2:].count('1')
            if count_1 % 2 == 0:
                count += 1
    return count


list_of_ips = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for i in range(int(input('Введите кол-во задач: '))):
    print('Тип №1: Поиск номера компьютера по маске и IP-адресу')
    print('Тип №2 Поиск минимального значения третьего байта IP-адреса слева')
    print('Тип №3 Поиск минимального значения четвёртого байта IP-адреса слева')
    print('Тип №4 Поиск наименьшего возможного кол-ва единиц в двоичной записи маски подсети')
    print('Тип №5 Поиск наибольшего возможного значения третьего байта слева маски сети')
    print('Тип №6 Поиск наибольшего возможного значения четвёртого байта слева маски сети')
    print('Тип №7 Поиск возможного количества масок')
    print('Тип №8 Поиск кол-ва IP-адресов, для которых сумма единиц в двоичной записи чётна')
    type_of_task = int(input('Введите тип задачи: '))
    if type_of_task == 1:
        input_mask = input('Введите маску: ')
        input_ip_node = input('Введите IP-адрес: ')
        b_mask = bin_of_ip(input_mask)
        b_ip_node = bin_of_ip(input_ip_node)
        print(number_of_PC(b_mask, b_ip_node))
    if type_of_task == 2:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(min_third_byte_of_mask(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 3:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(min_fourth_byte_of_mask(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 4:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(min_1(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 5:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(max_third_byte_of_mask(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 6:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(max_fourth_byte_of_mask(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 7:
        input_ip_node = input('Введите IP узла: ')
        input_ip_net = input('Введите IP сети: ')
        print(count_mask(input_ip_node, input_ip_net, list_of_ips))
    if type_of_task == 8:
        input_mask = input('Введите маску: ')
        input_ip = input('Введите IP-адрес: ')
        print(sum_of_1(input_ip, input_mask))


