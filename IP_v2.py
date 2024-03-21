sp_input_mask = [] # список IP-масок
sp_input_ip = [] # список IP-адресов

n = int(input('Кол-во задач: '))
for _ in range(n): # заполнение списков с клавиатуры
    sp_input_mask.append(input(f'Введите маску IP-адреса №{_ + 1}: '))
    sp_input_ip.append(input(f'Введите IP-адрес №{_ + 1}: '))

bin_masks = [] # список двоичных записей масок
bin_ips = [] # список двоичных записей IP-адресов

for i in range(n): # заполнение список двоичными записями

    parts_of_mask = sp_input_mask[i].split('.') # делим маску на байты
    bin_mask = ''
    for elem in parts_of_mask: # складываем все байты маски
        bin_of_part = bin(int(elem))[2:]
        bin_mask += '0' * (8 - len(bin_of_part)) + bin_of_part # добавление 0 для полной записи
    bin_masks.append(bin_mask) # добавляем двоичную запись в список

    parts_of_ip = sp_input_ip[i].split('.') # делим IP-адрес на байты
    bin_ip = ''
    for elem in parts_of_ip: # складываем все байты IP-адреса
        bin_of_part = bin(int(elem))[2:]
        bin_ip += '0' * (8 - len(bin_of_part)) + bin_of_part # добавление 0 для полной записи
    bin_ips.append(bin_ip) # добавляем двоичную запись в список

list_of_ip = [0, 128, 192, 224, 240, 248, 252, 254, 255]