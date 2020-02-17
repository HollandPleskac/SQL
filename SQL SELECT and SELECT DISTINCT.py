#sql lesson 4
#sqlite3 isnt cap sensitive
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
#regulars select command
##c.execute('SELECT Country From Students')
##for record in c.fetchall():
##    print(record)

#distinct select statement
c.execute('SELECT DISTINCT Country FROM Students')
for record in c.fetchall():
    print(record)
conn.commit()
c.close()
