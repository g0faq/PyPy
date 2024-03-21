words = set()


def parrot(phrase):
    global words
    if phrase in words:
        print(phrase)
    words.add(phrase)