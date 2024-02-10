import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS users;
''')
cursor.execute('''
    DROP TABLE IF EXISTS token;
''')

cursor.execute('''
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL,
               password TEXT NOT NULL,
               hash TEXT NOT NULL
           )
       ''')

cursor.execute('''
           CREATE TABLE IF NOT EXISTS token (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id TEXT NOT NULL,
               access_token TEXT NOT NULL,
               created_date TEXT NOT NULL
           )
       ''')