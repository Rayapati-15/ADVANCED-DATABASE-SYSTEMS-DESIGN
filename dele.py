import sqlite3

conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Students")

conn.commit()
conn.close()
