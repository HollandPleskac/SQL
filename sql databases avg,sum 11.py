#Avg/Sum 11
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

#exercise 1 - find the average gpa of all students
c.execute('Select AVG(GPA) From Students')
for record in c.fetchall():
    print(record)
#exercise 2 - find the sum of the gpa of all students

c.execute('SELECT SUM(gpa) FROM Students')
for record in c.fetchall():
    print(record)
    
conn.commit()
c.close()
