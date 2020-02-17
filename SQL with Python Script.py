#sql database set 2
import sqlite3
#conn=sqlite3.connect('example.db')
#c=conn.cursor()

#You use question marks as place holders for variables

name1='Vishal'
phone1='855-987-2342'
email1='vishal@gmail.com'
password1='123'

name2='Richard'
phone2='510-123-3456'
email2='richard@gmail.com'
password2='456'

name3='Holland'
phone3='510-111-2222'
email3='holland@gmail.com'
password3='111'

#creates a table
##c.execute('Create table users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)')

#deletes a table
##c.execute('DROP TABLE users')

#first way to insert data
##c.execute('INSERT INTO users(name, phone, email, password) \
##                  VALUES(?,?,?,?)', (name2,phone2, email2, password2))
##print('users inserted')

#second way to insert data
##c.execute('INSERT INTO users(name, phone, email, password) \
##                  VALUES(:name,:phone, :email, :password)',
##                  {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})
##print('users inserted')

#third way to insert data (multiple data points)
##users = [(name1,phone1, email1, password1),
##         (name2,phone2, email2, password2),
##         (name3,phone3, email3, password3)]
##c.executemany(' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)', users)
##print('users inserted')


#c.execute('SELECT name, email, phone FROM users')

#c.fetchone() selects one row - data is in list form
##user1=c.fetchone()
##print(user1[0])

#c.fetchall() selects all the rows - data is in a 2d list
##rows=c.fetchall()
##for r in rows:
##    print(r)

#update user with id1 in the following:
##newphone='431-421-5435'
##userid=1
##c.execute('UPDATE users SET phone=? WHERE id=?',(newphone,userid))

#delete user with id2 in the following:
##delete_userid=2
##c.execute('DELETE FROM users WHERE id=?', (delete_userid,))

#rollback any change to the database with this command (can omly rollback unsaved changes)
#conn.rollback()

#try except structure example
##try:
##    conn=sqlite3.connect('example.db')
##    c=conn.cursor()
##    c.execute('CREATE table \
##                        users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)')
##    conn.commit()
##except Exception as e:
##    conn.rollback()
##    print('rollback')
##finally:
##    c.close()

# try except structure example
conn=sqlite3.connect('example.db')
c=conn.cursor()
try:
    with conn:
        conn.execute('INSERT INTO users(name, phone, email, password) \
                  VALUES(?,?,?,?)', (name2,phone2, email2, password2))
except sqlite3.IntegrityError:
    print('Record already exists')
finally:
    c.close()


##conn.commit()
##c.close()
