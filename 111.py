import sqlite3

connection = sqlite3.connect(input())
cur = connection.cursor()

result = cur.execute("""SELECT title
FROM films
WHERE title LIKE '%Астерикс%' AND title NOT LIKE '%Обеликс%'""").fetchall()
for elem in result:
    print(elem[0])

connection.close()