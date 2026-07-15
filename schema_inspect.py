import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
print('tables:')
for row in cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table';"):
    print(row)
print('---')
print('orderDetails columns:')
for row in cur.execute('PRAGMA table_info(orderDetails);'):
    print(row)
conn.close()
