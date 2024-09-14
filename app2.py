import sqlite3
# Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('Ex2.db')
# Create a cursor object to interact with the database
cursor = connection.cursor()
cursor.execute('''CREATE TABLE Students (Id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')
cursor.execute("INSERT INTO Students (Id,Name, Grade) VALUES (118,'RUBY', 85.5)")
cursor.execute("INSERT INTO Students (Id,Name, Grade) VALUES (120,'Rambo', 90.0)")
cursor.execute("INSERT INTO Students (Id,Name, Grade) VALUES (122,'Rio', 87.5)")
cursor.execute("INSERT INTO Students (Id,Name, Grade) VALUES (124,'Sam', 70.5)")
cursor.execute("INSERT INTO Students (Id,Name, Grade) VALUES (126,'Jaggu', 90.5)")
cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()
for row in rows:
  print(row)
# Save (commit) the changes
connection.commit()
try:
  cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
  print(f"An error occurred: {e}")
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.3))
connection.close()
