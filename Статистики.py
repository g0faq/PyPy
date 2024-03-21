def print_statistics(arr):
    print(len(arr))
    if len(arr) != 0:
        print(sum(arr) / len(arr))
        print(float(min(arr)))
        print(float(max(arr)))
        arr.sort()
        if len(arr) % 2 != 0:
            print(float(arr[len(arr) // 2]))
        else:
            print(float((arr[len(arr) // 2] + arr[(len(arr) - 1) // 2]) / 2))
    else:
        print(0)
        print(0)
        print(0)
        print(0)