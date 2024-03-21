def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('Это треугольник')
    else:
        print('Это не треугольник')


# a, b, c = int(input()), int(input()), int(input())
# triangle(a, b, c)