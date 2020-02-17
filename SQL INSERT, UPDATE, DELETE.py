#07: INSERT, UPDATE, DELETE
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
"""to insert data in a table
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * syntax - Insert  into table_name (column1, column2, column3, …) values ( value1, value2, value3,…)
 * example - INSERT INTO Students (StudentName,ParentName, City,Country  , GPA, dateStarted) VALUES ("Neel Reina","Vishal Reina","Pleasanton","USA",3.90,"2016-08-15"));
 * example is meant to be executed in terminal
"""

#Program Inserts my data into the students table
##c.execute('INSERT INTO Students (StudentName, ParentName, City, Country, GPA, dateStarted) VALUES ("Holland Pleskac", "Doug Pleskac", "Mountain House", "USA", "10000000.0", "2100-01-01")')
##c.execute('SELECT * FROM Students')
##for record in c.fetchall():
##    print(record)


"""to change data in a table
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * syntax - UPDATE table_name SET column1=value1, column2=value2,... WHERE condition;
 * without the WHERE clause - all values in the table will be updated
 * example is meant to be executed in terminal
"""

#Program updates parent name of "James Tang" to "new parent"
##c.execute('UPDATE Students SET ParentName="new parent" WHERE studentName = "James Tang" AND country = "China"')
##c.execute('SELECT * FROM Students')
##for record in c.fetchall():
##    print(record)

#Program updates first student(studentID = "1") with new city("Majic Mountain") and new country("Disney Land")
##c.execute('UPDATE Students SET Country="Disney Land", City = "Magic Mountain" WHERE StudentId = "1"')
##c.execute('SELECT * FROM Students')
##for record in c.fetchall():
##    print(record)

"""to delete data from the table
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * syntax - DELETE From table_name WHERE conditions;
 * example is meant to be executed in terminal
"""
#Program deletes "Tanya Anand" from the student table
##c.execute('DELETE FROM Students WHERE StudentName = "Tanya Anand"')
##c.execute('SELECT * FROM Students')
##for record in c.fetchall():
##    print(record)
    
conn.commit()
c.close()

