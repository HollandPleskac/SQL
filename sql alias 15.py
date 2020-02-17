#sql alias 15
##SQL Aliases are used to give a table, or column in a table, a temporary name

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

#example
#used when you think the name is too long
##c.execute('SELECT studentid as id, studentname as name from students')
##for record in c.fetchall():
##    print(record)

#exercise 1: create two aliases, one for teh studentname column and one for the parent name column
##c.execute('SELECT studentname as sname, parentname as pname from students')
##for record in c.fetchall():
##    print(record)

#exercise 2 : create an alies named 'name' that combines for columns ( studentname, city, and country )
c.execute('Select StudentName, City, country as name from students')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
