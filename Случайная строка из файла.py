from random import choice

with open("lines.txt", encoding='utf-8') as file:
    data = file.readlines()
if data:
    print(choice(data))