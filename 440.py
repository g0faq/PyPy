import random

n = int(input('количество чисел в списке:'))

squares = []  # список квадратов
power_5 = []  # список степеней пяти
prime_numbers = []  # список простых чисел
all_numbers = [] # список всех чисел

# управляемый рандом
def rand_driven(n):
    count = 0
    while count != n:
        x = random.randint(1, 10000)

        # проверка на простое число
        f = False
        if x == 1 or x == 2:
            f = True
        else:
            for i in range(2, x):
                if x % i != 0:
                    f = True
                else:
                    f = False
                    break
        if f:
            all_numbers.append(x)
            prime_numbers.append(x)
            count += 1

        # проверка на квадрат
        if x ** 0.5 == int(x ** 0.5):
            all_numbers.append(x)
            squares.append(x)
            count += 1

        # проверка на степень пяти
        if x % 5 == 0:
            f = False
            x1 = x
            while x1 != 1:
                if x1 % 5 != 0:
                    break
                x1 //= 5
            if x1 == 1:
                f = True
            if f:
                all_numbers.append(x)
                power_5.append(x)
                count += 1
    return all_numbers, squares, power_5, prime_numbers


all_numbers = rand_driven(n)[0]
squares = rand_driven(n)[1]
power_5 = rand_driven(n)[2]
prime_numbers = rand_driven(n)[3]

# подсчёт максимального количества подряд идущих квадратов (решение №1)
def max_len_squares():
    count = 0
    max_count = 0
    for elem in all_numbers:
        if elem in squares:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# подсчёт максимального количества подряд идущих степеней пяти (решение №1)
def max_len_power_5():
    count = 0
    max_count = 0
    for elem in all_numbers:
        if elem in power_5:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# подсчёт максимального количества подряд идущих простых чисел (решение №1)
def max_len_prime_numbers():
    count = 0
    max_count = 0
    for elem in all_numbers:
        if elem in prime_numbers:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# вывод решения №1
print(f'Тест №1. Максимальное количество квадратов, идущих подряд: {max_len_squares()}')
print(f'Тест №1. Максимальное количество степеней пяти, идущих подряд: {max_len_power_5()}')
print(f'Тест №1. Максимальное количество простых чисел, идущих подряд: {max_len_prime_numbers()}')

print('-' * 65)

# подсчёт максимального количества подряд идущих квадратов (решение №2)
def max_len_squares_1():
    count = 0
    max_count = 0
    for elem in all_numbers:
        if elem == int(elem ** 0.5) ** 2:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# подсчёт максимального количества подряд идущих степеней пяти (решение №2)
def max_len_power_5_1():
    count = 0
    max_count = 0
    for elem in all_numbers:
        if elem % 5 == 0:
            f = False
            elem1 = elem
            while elem1 != 1:
                if elem1 % 5 != 0:
                    break
                elem1 //= 5
            if elem1 == 1:
                f = True
            if f:
                count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# подсчёт максимального количества подряд идущих простых чисел (решение №2)
def max_len_prime_numbers_1():
    count = 0
    max_count = 0
    for elem in all_numbers:
        f = False
        if elem == 1 or elem == 2:
            f = True
        else:
            for i in range(2, elem // 2):
                if elem % i != 0:
                    f = True
                else:
                    f = False
                    break
        if f:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

# вывод решения №2
print(f'Тест №2. Максимальное количество квадратов, идущих подряд: {max_len_squares_1()}')
print(f'Тест №2. Максимальное количество степеней пяти, идущих подряд: {max_len_power_5_1()}')
print(f'Тест №2. Максимальное количество простых чисел, идущих подряд: {max_len_prime_numbers_1()}')