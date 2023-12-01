import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks INTEGER
    )
''')


data_to_insert = [
    (1, 'John', 30,99),
    (2, 'Alice', 25,100),
    (3, 'Bob', 28,2),
]

cursor.executemany('INSERT INTO my_table (id, name, age, marks) VALUES (?, ?, ?, ?)', data_to_insert)
res = cursor.execute('SELECT name from my_table ')
print(res.fetchall())
res  = cursor.execute('DELETE FROM my_table WHERE id = 2')
print(res.fetchall())
res = cursor.execute('UPDATE  my_table SET id =7 where name = "Bob"')
print(res.fetchall())
res = cursor.execute('SELECT * from my_table ')
print(res.fetchall())
conn.commit()
conn.close()