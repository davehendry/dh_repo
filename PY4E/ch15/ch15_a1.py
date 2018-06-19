import sqlite3

conn = sqlite3.connect('py4e.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Tracks')
# cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')
# conn.close()

# cur.execute('DELETE FROM Ages')
# cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Nadeem', 19))
# cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Chenille', 40))
# cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Mutinta', 31))
# cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Ricards', 33))
# conn.commit()

print('Ages:')
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
     print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()
# cur.close()