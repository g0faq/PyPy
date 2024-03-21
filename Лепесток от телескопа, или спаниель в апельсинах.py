import sys

slovo = input()
words = map(str.strip, sys.stdin)
list_words = []
for elem in words:
    new_slovo = slovo
    ok = True
    for letter in elem:
        i = new_slovo.find(letter)
        if i != -1:
            new_slovo = new_slovo[:i] + new_slovo[i + 1:]
        else:
            ok = False
            break
    if ok:
        list_words.append(elem)
print(len(list_words))
for elem in list_words:
    print(elem)