import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

conn.commit()
conn.close()
