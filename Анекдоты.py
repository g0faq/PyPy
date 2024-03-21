s = set()


def print_only_new(message):
    if message not in s:
        print(message)
    s.add(message)