import sqlite3 as sql
 
db = sql.connect('testserver.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    fio TEXT

)""")
db.commit()

user_fio = input('Fio: ')
user_email = input('Email: ')
user_password = input('Password: ')
cur.execute("SELECT login FROM users WHERE login = '{user_fio}'")
if cur.fetchone() is None:
    cur.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_fio, user_email, user_password))
    db.commit()
    print('Успех')
else:
    print('Такая запись уже имеется!')

 
 