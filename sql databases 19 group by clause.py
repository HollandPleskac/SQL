#19 group by clause sql
##The GROUP BY statement is often used with aggregate functions(COUNT,MAX MIN, SUM, AVG) to group the result-set by one or more columns.

##GROUP BY Syntax:


##SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);

import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

#sql group by examples
##c.execute('select count(studentID), country from students group by country')
##for record in c.fetchall():
##    print(record)
#exercise 1 list the number of students in each country, sorted high to low
##c.execute('select count(studentID), country from students group by country order by country desc')
##for record in c.fetchall():
##    print(record)

#exercise 2 list the number of classnames taken by each students in classes
##c.execute('select count(classname), studentID from classes group by classname order by studentID asc')
##for record in c.fetchall():
##    print(record)

#exercise 3 list the number of numbers of classes taken by each student inner join
c.execute('select count(studentID), classname from classes group by studentID order by classname')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
