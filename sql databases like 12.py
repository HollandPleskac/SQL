# like 12
##The LIKE is used in a WHERE clause to find for specified pattern in a column.
##
##There are two wildcards used in conjunction with the LIKE operator:
##
##% presents zero, one, or multiple character.
##
##_ presents a single character.

##LIKE Operator                              | Description
##WHERE studentName LIKE 'a%'     | Find any values that starts with 'a'
##WHERE studentName LIKE '%a'     | Find any values that ends with 'a'
##WHERE studentName LIKE '%ab%'| Find any values that have 'ab' in any position
##WHERE studentName LIKE '_r%'   | Find any values that have in the second position
##WHERE studentName LIKE 'a_%_%'| Find any values that starts with 'a' and are at least three characters in length 
##WHERE studentName LIKE 'a%o'     | Find any values that starts with 'a' and ends with 'o'


import sqlite3
conn = sqlite3.connect('example.db')
c=conn.cursor()

#exercise 1 - select all students where the city starts with a B,S, or M
##c.execute('Select StudentName,City From Students Where City like "B%" or City like "S%" or City like "M%"')
##for record in c.fetchall():
##    print(record)

#exercise 2 - find all students where the city starts with a 'B', followed by any char, followed by an 'n', followed by any char, followed by an 'a'
##c.execute('Select StudentName,City From Students Where City like "B_n_a%"')
##for record in c.fetchall():
##    print(record)

#exercise 3 - find all students with a city ending with 'hai'
##c.execute('Select StudentName,City From Students Where City like "%hai"')
##for record in c.fetchall():
##    print(record)

#exercise 4 - find all students with a city containing i
##c.execute('Select StudentName,City From Students Where City like "%i%"')
##for record in c.fetchall():
##    print(record)

#exercise 5 - find all students in a city starting with 'San'
##c.execute('Select StudentName,City From Students Where City like "San%"')
##for record in c.fetchall():
##    print(record)

#exercise 6 - find all students with a student name that doesn't start with an A
##c.execute('Select StudentName From Students Where StudentName Not like "A%"')
##for record in c.fetchall():
##    print(record)

#exercise 7 - find all students with a parentName that stars with 'A' and ends with 'y'
##c.execute('Select StudentName,ParentName From Students Where parentName like "A%y"')
##for record in c.fetchall():
##    print(record)

#exercise 8 : find all students with a student name that starts with 'A' and is at least 3 characters in length
##c.execute('Select StudentName From Students Where StudentName like "A_%_%"')
##for record in c.fetchall():
##    print(record)

#exercise 9 : find all students with a student name that has an a in the second position
##c.execute('Select StudentName From students where StudentName like "_a%"')
##for record in c.fetchall():
##    print(record)

#exercise 10 : find all students with a studentName that has 'ar' in any position
##c.execute('Select StudentName From Students Where StudentName like "%ar%"')
##for record in c.fetchall():
##    print(record)

#exercise 11 : find all students with a student name ending with 'a'
##c.execute('select studentName from students where studentname like "%a"')
##for record in c.fetchall():
##    print(record)

#exercise 12: find all students with a studentname starting with 'a'
##c.execute('Select studentName from students where studentname like "%a"')
##for record in c.fetchall():
##    print(record)

#exercise 13: find all students with a city not starting with B,S, or M
##c.execute('Select studentName,City From Students Where city not like "B%" and city not like "S%" and city not like "M%"')
##for record in c.fetchall():
##    print(record)

#exercise 14: find all students with a city starting with B or D
c.execute('Select studentname,city From Students Where city like "B%" or city like "D%"')
for record in c.fetchall():
    print(record)


conn.commit()
c.close
