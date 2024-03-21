def check_mask(mask, number):
    digits_mask = list(mask)
    digits_numbers = list(str(number))
    axis = 0

    for i in range(len(digits_mask)):
        if digits_mask[i] == '*':
            axis += len(digits_numbers) - len(digits_mask)
        elif digits_mask[i] != digits_numbers[i + axis] and digits_mask[i] != '?':
            return False

    return True


def find_numbers(mask, divider, max_value):
    result = []

    def generate_numbers_recursively(prefix, remaining_wildcards):
        if remaining_wildcards == 0:
            num = int(prefix)
            if num <= max_value and num % divider == 0:
                result.append(str(num))
            return

        for digit in range(10):
            new_prefix = prefix + str(digit)
            generate_numbers_recursively(new_prefix, remaining_wildcards - 1)

    wildcards_count = mask.count('*') + mask.count('?')
    generate_numbers_recursively("", wildcards_count)

    return result


def print_answer(mask, divider, max_value):
    answer = find_numbers(mask, divider, max_value)

    if not answer:
        print("No numbers found.")
        return

    print("\033[1m\033[32m{}".format('ANSWER'))
    for element in answer:
        print(element)


input_mask = input()
input_max_value = int(input())
input_divider = int(input())

print_answer(input_mask, input_divider, input_max_value)
