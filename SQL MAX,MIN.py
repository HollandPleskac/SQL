#09 MAX, MIN
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()

#MIN() syntax
    #SELECT MIN(column_name) FROM table_name WHERE condition;
    #MIN() finds the smallest value of the selected column

#exercise 1 - find a student who has the lowest gpa and lives in the USA
##c.execute('SELECT StudentName, MIN(gpa) FROM Students WHERE country = "USA"')
##for record in c.fetchall():
##    print(record)

#exercise 2 - latest datestarted from students
##c.execute('SELECT StudentName, MAX(datestarted) FROM Students')
##for record in c.fetchall():
##    print(record)

#exercise 3 - find the student with the highest gpa from india
##c.execute('SELECT StudentName, MAX(gpa) FROM Students WHERE country="India"')
##for record in c.fetchall():
##    print(record)

#exercise 3 - find all the detals of the student with the highest gpa queries
c.execute('SELECT * FROM Students WHERE gpa=(SELECT MAX(gpa) FROM Students)')
for record in c.fetchall():
    print(record)
conn.commit()
c.close()
