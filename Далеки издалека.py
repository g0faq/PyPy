import sys

sentenses = map(str.strip, sys.stdin)
count = 0
for element in sentenses:
    element = element.lower()
    words = element.split()
    for elem in words:
        if elem.startswith('далек'):
            count += 1
            break
print(count)
