import sqlite3
connection = sqlite3.connect("users.db")

cursor = connection.cursor()

command = "CREATE TABLE IF NOT EXISTS users(id TEXT, name TEXT, email TEXT, Position TEXT, password TEXT) "

cursor.execute(command)