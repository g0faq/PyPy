def digits_from_mask(mask):
    digits, numbers = [], []
    string = ''

    for i in range(len(mask)):
        elem = mask[i]

        if elem == '?' or elem == '*':
            if len(string) != 0:
                digits.append(string)
                numbers.append(string)
            digits.append(elem)
            string = ''

        else:
            string += elem

        if i == len(mask) - 1 and len(string) != 0:
            digits.append(string)
            numbers.append(string)

    return digits, numbers


def list_numbers(mask, numbers, number):
    check = []
    number = str(number)

    for elem in numbers:
        if elem not in number:
            return False

    for i in range(len(numbers) - 1):
        elem = numbers[i]

        if i == 0:
            check.append(number[:number.index(elem)])
            check.append(elem)

        check.append(number[number.index(elem) + len(elem):number.index(numbers[i + 1])])
        check.append(number[number.index(numbers[i][0]):number.index(numbers[i][-1]) + 1])

    if len(check) != 0 and check[0] == '':
        check = check[1:]

    if mask[-1] == '?' or mask[-1] == '*':
        check.append(number[number.index(numbers[-1]) + len(numbers[-1]):])

    return check


def checking(mask, number, digits_mask, dn):
    result_checking = list_numbers(mask, dn, number)

    if result_checking:
        for i in range(len(digits_mask)):
            digit_m, digit_n = digits_mask[i], result_checking[i]

            if digit_m == '?':
                if len(digit_n) != 1:
                    return False

            elif digit_m != '*' and digit_m != digit_n:
                return False

        return True
    return False


def find_numbers(mask, max_value, divider, dm, dn):
    s_v = ''
    if mask.count('*') != 0:
        s_v = mask.replace('*', '')
    if mask.count('?') != 0:
        if len(s_v) != 0:
            s_v = s_v.replace('?', '0')
        else:
            s_v = mask.replace('?', '0')

    start_value = int(s_v)

    result = []

    for number in range(start_value, max_value + 1):
        if checking(mask, number, dm, dn):
            if number % divider == 0:
                result.append([number, number // divider])

    return result


m = '1?7602*0'
result_digits_from_mask = digits_from_mask(m)
d_m, d_n = result_digits_from_mask[0], result_digits_from_mask[1]


print(find_numbers('1?7602*0', 1176020, 1, d_m, d_n))
