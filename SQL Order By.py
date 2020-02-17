#06: ORDER BY
#ORDER BY keyword is used to sort the record in ascending order by default
#DESC keyword is used to sort the record in descending order using
import sqlite3

conn=sqlite3.connect('example.db')
c=conn.cursor()

#sort can be by abc order, number order, dates
# putting DESC at the end reverses the order

#prints the fields of students in descending order by studentid
##c.execute('SELECT * FROM Students ORDER BY "StudentID" DESC;')
##for record in c.fetchall():
##    print(record)

#prints all students from the student table sorted by studentname (sorted in ABC order)
##c.execute('SELECT * FROM Students ORDER BY "StudentName";')
##for record in c.fetchall():
##    print(record)

#prints all students from the student table sorted by their city in descending order
##c.execute('SELECT * FROM Students ORDER BY "city" DESC;')
##for record in c.fetchall():
##    print(record)

#prints all students who live in India from students table sorted by gpa
##c.execute('SELECT * FROM Students ORDER BY "gpa";')
##for record in c.fetchall():
##    print(record)

#prints all students who live in USA or China from Students table sorted by started class time and sorted by gpa
#first ORDER By takes priority
c.execute('SELECT * FROM Students WHERE country = "USA" OR country = "China" ORDER BY "dateStarted" DESC ,"gpa";')
for record in c.fetchall():
    print(record)
