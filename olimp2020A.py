k = int(input())
n = int(input())

print(min(abs(k * (n // k) - n), abs(k * ((n // k) + 1) - n)))
