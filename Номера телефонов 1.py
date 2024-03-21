def numbers(num):
    sp = ['-', ')', '(']
    a = ''
    number = ''.join(num.split())
    try:
        if number[0] == '8' or number[:2] == '+7':
            if number[0] == '8':
                number = '+7' + number[1:]
        else:
            raise ValueError
        if (number.count('(') != number.count(')') or
                number.count('(') > 1 or number.count(')') > 1):
            raise ValueError
        if '--' in number or number[0] == '-' or number[-1] == '-':
            raise ValueError
        for elem in number:
            if elem not in sp:
                a += elem
    except ValueError:
        return 'неверный формат'
    if len(a) != 12:
        return 'неверное количество цифр'
    return a


num = input()
print(numbers(num))