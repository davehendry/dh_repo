import sqlite3

conn = sqlite3.connect('music_lib_db.sqlite')
cur = conn.cursor()
name = 'Pank Floyd'

cur.execute('SELECT name FROM Artist WHERE name = ? ', (name, ))
row = cur.fetchone()
print(row)