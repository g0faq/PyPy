def dividers(number):
    count = 2
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    return count


def max_dividers(value):
    result = 0
    for i in range(value):
        result = max(result, dividers(i))

    return result


def find_answer(max_value):
    res = []
    for num in range(max_value):
        if dividers(num) >= max_dividers(num):
            res.append(num)

    return res[-5:]


a = 1
for i in range(1, 10):
    a *= i
    print(a)
print(find_answer(10000))