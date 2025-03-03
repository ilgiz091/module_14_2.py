import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     cursor.execute(
#     'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#     (f'User{i}', f'example{i}@gmail.com', i*10, 1000)
#     )

# cursor.execute('UPDATE Users SET balance = 500 WHERE id IN (SELECT id FROM Users WHERE (ROWID % 2) = 1)')

# cursor.execute('DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE (ROWID % 3) = 1)')

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
# users = cursor.fetchall()
# for user in users:
#     username, email, age, balance = user
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(total_users)

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances)

print(all_balances / total_users)

connection.commit()
connection.close()