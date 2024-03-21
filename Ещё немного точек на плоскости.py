left = (0, 0)
right = (0, 0)
top = (0, 0)
bottom = (0, 0)
f = True
for i in range(int(input())):
    x, y = map(int, input().split())
    if f:
        f = False
        left = (x, y)
        right = (x, y)
        top = (x, y)
        bottom = (x, y)
    if abs(x) > abs(y):
        print(f'({x}, {y})')
        if x < left[0]:
            left = (x, y)
        elif x > right[0]:
            right = (x, y)
        if y < bottom[1]:
            bottom = (x, y)
        elif y > top[1]:
            top = (x, y)
    else:
        if x < left[0]:
            left = (x, y)
        elif x > right[0]:
            right = (x, y)
        if y < bottom[1]:
            bottom = (x, y)
        elif y > top[1]:
            top = (x, y)
print(f'left: ({left[0]}, {left[1]})')
print(f'right: ({right[0]}, {right[1]})')
print(f'top: ({top[0]}, {top[1]})')
print(f'bottom: ({bottom[0]}, {bottom[1]})')