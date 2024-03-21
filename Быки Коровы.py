import sqlite3

con = sqlite3.connect('Bulls_and_cows.sqlite')
cur = con.cursor()
# cur.execute("""DELETE from bknum""")
for i in range(100, 1000):
    if str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2]:
        cur.execute("""INSERT INTO bknum(number) VALUES(?)""", (str(i), ))


con.commit()
con.close()
