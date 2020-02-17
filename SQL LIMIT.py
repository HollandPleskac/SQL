#08: LIMIT
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()

#SQL LIMIT is used to select the top number records from the table

#Program prints all the fields of the top three records from students table
##c.execute('SELECT * FROM Students LIMIT 3')
##for record in c.fetchall():
##    print(record)
    

#Program prints the first four students whose gpa are greater than or equal 4 and live in India
##c.execute('SELECT * FROM Students WHERE gpa >= "4" AND country = "India" LIMIT 4')
##for record in c.fetchall():
##    print(record)

#Program prints the first five students whose gpa is greater than 4 from the Students table
##c.execute('SELECT * FROM Students WHERE gpa > "4" LIMIT 5')
##for record in c.fetchall():
##    print(record)

#Program prints the first three students who live in the USA
##c.execute('SELECT * FROM Students WHERE country = "USA" LIMIT 3')
##for record in c.fetchall():
##    print(record)
    
conn.commit()
c.close()
