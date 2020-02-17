#Different Types of JOIN 17
#just made a new database called database.db
#deleted code that made it but it was just a bunch of insert statements
import sqlite3
conn = sqlite3.connect('database.db')
c=conn.cursor()
c.execute('select * from classes')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
print('these tables have been created successfully')
