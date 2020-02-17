#inner join clause 16
# an inner join keyword finds records that have matching values in both tables
#if the keyword isn't in both tables it doesn't get printed out

#syntax:
#SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

#exercise 1 : find all classes with students information
##c.execute('SELECT Classname FROM Classes INNER JOIN Students ON Classes.StudentID = Students.StudentID')
##for record in c.fetchall():
##    print(record)

#exercise 2 : find matching values that have matching values in 3 tables
c.execute('SELECT StudentName FROM ((students INNER JOIN teachers ON students.studentID = teachers.teacherID) INNER JOIN classes ON students.studentID = classes.studentID)')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
