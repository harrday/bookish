import sqlite3
from sqlite3 import Error

# Create the sqlite database if it does not exist. If it exist, connect to it.
try:
    conn = sqlite3.connect('database.db')
except Error as e:
    print(e)

cursor = conn.cursor()

sql_command = '''
    CREATE TABLE IF NOT EXISTS contacts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Firstname TEXT, 
        Lastname TEXT, 
        Email TEXT
    )'''
cursor.execute(sql_command)
conn.commit()
insert_data = """
    INSERT INTO contacts 
    (Firstname, Lastname, Email) 
    VALUES (
        'David',
        'Attenborough',
        'dattenborough@example.com'
    )
"""
cursor.execute(insert_data)
conn.commit()

select_data = 'SELECT * FROM contacts'
cursor.execute(select_data)

rows = cursor.fetchmany(5)  # select 5 lines

for row in rows:
    print(row)
conn.close()