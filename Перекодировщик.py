slovarik = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo",
            "Й": "J", "Ц": "C", "У": "U", "К": "K", "Е": "E", "Н": "N",
            "Г": "G", "Ш": "Sh", "Щ": "Shh", "З": "Z", "Х": "H", "Ъ": "#",
            "Ф": "F", "Ы": "Y", "В": "V", "А": "A", "П": "P", "Р": "R",
            "О": "O", "Л": "L", "Д": "D", "Ж": "Zh", "Э": "Je", "Я": "Ya",
            "Ч": "Ch", "С": "S", "М": "M", "И": "I", "Т": "T", "Ь": "'",
            "Б": "B", "Ю": "Ju", "Ё": "Jo"}
file = open("cyrillic.txt", 'r', encoding='utf8')
read_file = file.read()
spisochek = []
for elem in read_file:
    if elem in slovarik:
        spisochek.append(slovarik[elem])
    else:
        spisochek.append(elem)
file.close()
file2 = open('transliteration.txt', 'r', encoding='utf8')
file2 = ''.join(spisochek)
