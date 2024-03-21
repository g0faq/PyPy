def checking(n, a, b):
    for i in range(n):
        if a[i] != 0 and b[i] != 0:
            return True
    return False


def vvvllra(m, e, w):
    list_a, list_b = e, w
    min_b = 1
    while checking(m, list_a, list_b):


    return sum(list_a) - sum(list_b)


input_n = int(input())
input_a = list(map(int, input().split()))
input_b = list(map(int, input().split()))

print(vvvllra(input_n, input_a, input_b))
