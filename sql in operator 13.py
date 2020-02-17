#sql in operator  13

##SELECT column_name(s) FROM table_name WHERE column_name IN (value1, value2, ...);

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

#exercise 1 : find all students that are located in 'usa', 'india', or 'south korea'
##c.execute('Select studentname,country From Students Where country in ("USA","India","South Korea")')
##for record in c.fetchall():
##    print(record)

#exercise 2 : find all students that are not located in india or the usa
##c.execute('Select studentname,country From Students Where country not in ("USA","India")')
##for record in c.fetchall():
##    print(record)


#exercise 3 : find all students that are from the same countries as the teachers
'''
SELECT column_name(s)
FROM table_name 1
WHERE column_name IN (SELECT column_name FROM table_name 2);
the format is a nested for loop -
for each country
    for each student
         if student in country:
              print the student
'''
c.execute('Select StudentName,country From Students Where country in (Select country From teachers)')
for record in c.fetchall():
    print(record)
# the teachers are from India, China, and the USA - the code prints out all the students that are from these countries

conn.commit()
c.close()
