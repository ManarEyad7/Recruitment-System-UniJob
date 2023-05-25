import sqlite3
connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('1905480', 'Manar Eyad',      '1905480@uj.edu.sa', 'student', 'Aa@123456')")
cursor.execute("INSERT INTO users VALUES ('2005892', 'Ranya Alghamdi',  '2005892@uj.edu.sa', 'student', 'Aa@123456')")
cursor.execute("INSERT INTO users VALUES ('1905453', 'Sumaia Ahmed',    '1905453@uj.edu.sa', 'student', 'Aa@123456')")
cursor.execute("INSERT INTO users VALUES ('2006786', 'Raneem Aljadani', '2006786@uj.edu.sa', 'student', 'Aa@123456')")

cursor.execute("INSERT INTO users VALUES ('4514542', 'ELHAM ALGAMDI ', 'ealghamdi2@uj.edu.sa', 'employee', 'Aa@123456')")

connection.commit()
