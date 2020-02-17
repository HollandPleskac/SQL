#10 Count
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()

#returns the number of distinct(different) values of the specific column
##c.execute('SELECT COUNT(DISTINCT studentname) FROM Students')
##for record in c.fetchall():
##    print(record)

#finds the number of students
##c.execute('SELECT COUNT(studentid) FROM Students')
##for record in c.fetchall():
##    print(record)

#counts the number of classes
conn.commit()
c.close()
