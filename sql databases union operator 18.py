#18 union operator
#The UNION operator is used to combine the result-set of two or more SELECT statements.

#Each SELECT statement with UNOIN must have the same number of columns

#The columns must also have similar data types

#The columns in each SELECT statement must also be in the same order.

#UNION Syntax:
##SELECT column_name(s) FROM table1 UNION SELECT column_name(s) table2;

#The UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL

import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

#exercise1 select all the different countries (only distinct values) from students and teachers
##c.execute('SELECT country FROM students UNION select country FROM teachers ORDER BY country')
##for record in c.fetchall():
##    print(record)

#exercise2 select all the different USA cities(only distinct values) from students and teachers
##c.execute('SELECT city FROM students  WHERE country="USA" UNION select city FROM teachers WHERE COUNTRY="USA" ORDER BY city')
##for record in c.fetchall():
##    print(record)

# exercise3 select all different usa cities (duplicated distinct values) from studentsa nd teachers
c.execute('Select city from students where country="USA" UNION ALL select city from teachers where country="USA" order by city')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
