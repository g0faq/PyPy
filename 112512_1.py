from collections import defaultdict

# Считываем данные из файла
sp_input = [x[:-1] for x in list(open('input.txt').readlines())]
symbols = '.,:;!?'

# Создаем словарь для подсчета частоты слов
word_count = defaultdict(int)
# Подсчитываем частоту слов
for line in sp_input:
    words = line.split()
    for word in words:
        word = word[:-1] if word[-1] in symbols else word
        word_count[word.lower()] += 1
        print(word_count)

# Сортируем слова по убыванию частоты и алфавиту
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# Записываем результаты в файл
with open('output.txt', 'w') as f:
    for word, count in sorted_words:
        f.write(f"{word} {count}\n")
