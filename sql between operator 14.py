#sql between operator 14
##SELECT column_name(s) FROM table_name 
##WHERE column_name BETWEEN value1 AND value2;

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

#example
##c.execute('SELECT * FROM Students Where DateStarted BETWEEN "2013-01-01" AND "2017-12-31"')
##for record in c.fetchall():
##    print(record)

#exercise 1 : find all students with a gpa between 2.0 and3.0
##c.execute('SELECT studentname, gpa FROM Students Where gpa BETWEEN "2.0" AND "3.0"')
##for record in c.fetchall():
##    print(record)

#exercise 2 : find all students with a gpa between 3.0 and 4.0 - in addition dont how students with a studentID of 1,2, or 3
##c.execute('Select studentid,studentname,gpa from students where gpa between "3.0" and "4.0" AND StudentID != "3" AND StudentID != "2" AND StudentID != "1"')
##for record in c.fetchall():
##    print(record)

#exercise 3 : find all students with a student name not between "ankit Babuand" and "James Tang"
c.execute('Select studentname from students where studentname not between "Ankit Babu" and "James Tang"')
for record in c.fetchall():
    print(record)

print()

#exercise 4 : find all students with a student name between ankit babu and James Tang
c.execute('Select studentname from students where studentname between "Ankit Babu" and "James Tang"')
for record in c.fetchall():
    print(record)
conn.commit()
c.close()
