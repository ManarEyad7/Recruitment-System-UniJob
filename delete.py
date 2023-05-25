import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM users WHERE id = '1905453'")


connection.commit()