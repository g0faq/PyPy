import random

n = int(input())

squares = []  # список квадратов
power_5 = []  # список степеней пяти
prime_numbers = []  # список простых чисел

# управляемый рандом
all_numbers = []


def rand_driven(n):
    count = 0
    while count != n:
        x = random.randint(1, 101)

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

print(f'Максимальное количество квадратов, идущих подряд: {max_len_squares()}')
print(f'Максимальное количество степеней пяти, идущих подряд: {max_len_power_5()}')
print(f'Максимальное количество простых чисел, идущих подряд: {max_len_prime_numbers()}')