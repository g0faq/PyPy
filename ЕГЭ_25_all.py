def check_mask(mask, number):

    digits_mask = list(mask)
    digits_numbers = list(str(number))

    axis = 0

    if mask.count('*') == 1:
        for i in range(len(digits_mask)):
            if digits_mask[i] == '*':
                axis += len(digits_numbers) - len(digits_mask)
            elif digits_mask[i] != digits_numbers[i + axis] and digits_mask[i] != '?':
                return False

    return True


def find_numbers(mask, divider, max_value):

    start_value = int(mask.replace('*', '').replace('?', '0'))

    result = []

    for i in range(start_value, max_value + 1):
        if check_mask(mask, i):
            if i % divider == 0:
                result.append(str(i))

    return result


def print_answer(mask, divider, max_value):

    answer = find_numbers(mask, divider, max_value)

    for element in answer:
        output = element
        print("\033[1m\033[32m{}".format('ANSWER'), output)


input_mask = input()
input_max_value = int(input())
input_divider = int(input())

print_answer(input_mask, input_divider, input_max_value)
