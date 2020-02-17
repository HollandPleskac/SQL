#20 having clause sql databases
##The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
#inner join joins two tables which have the same column
import sqlite3
conn = sqlite3.connect('database.db')

from pprint import pprint

c = conn.cursor()

#example 1
#List the number of students in country. Only include countries with more than 5 students.
##c.execute('SELECT COUNT(StudentID), Country FROM students GROUP BY Country HAVING COUNT(studentId) >5')
##for record in c.fetchall():
##    print(record)

#exercise 1
#List the teachers that have teaches more than 3 classes. - gives the user the option for different groupings
##headers = []
##group_choice = 'country'
##res = c.execute('PRAGMA table_info(teachers)')
##for info in res:
##    headers.append(info)
##a = input('enter the column that you want to group by :')
##c.execute('select teachername from teachers inner join classes on teachers.teacherid = classes.teacherid group by ' + a +' having count(classes.teacherid) > 3')
##for record in c.fetchall():
##    print(record)


#checks all the teachers who teacher classes
##c.execute('select teachername from teachers inner join classes on teachers.teacherid = classes.teacherid')
##for record in c.fetchall():
##    print(record)

#exercise 2
#list the students who have taken more than 3 classes
##c.execute('select studentname,students.studentid from students inner join classes on students.studentid = classes.studentid group by country having count(classes.studentid) > 3')
##for record in c.fetchall():
##    print(record)

#exercise 3
#List a number of the students who have gotten GPA greater than or equal 2.0.
# the program prints the amount of students who have gpa greater than 2.0 - results are organized into amount individual gpa values
c.execute('select count(studentid), gpa from students group by gpa having gpa >= 2.0')
##c.execute('select country, studentname, gpa from students')
for record in c.fetchall():
    pprint(record, indent=4)
conn.commit()
c.close()
