#INTERACTIVE SQL v1
import sqlite3

#quick note - headers is for creating a table and header is for adding to a table
headers=['ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT']

def database():
    conn=sqlite3.connect(input('database name:' )+'.db')
    #c is the cursor for  the database connection
    c = conn.cursor()
    return conn, c

def dbClose(c):
    c.close()
    

def createHeader():
    choice = input('make another header(y/n): ')
    if choice == 'y':
        header = input('name of header: ')
        headers.append(header)
        createHeader()
    elif choice == 'n':
        print()

def createTable(c, con):
    print('enter headers for your table..')
    header = input('name of header: ')
    headers.append(header)
    createHeader()
    table = 'CREATE TABLE ' + (input('name of table: ').replace(" ","")) + ' (' + (','.join(headers)) + ')' 
    c.execute(table)       
    con.commit()
        

def addtoTable(c, con):
    header = []
    values = []
    table_name = input('name of table: ')
    res = c.execute('PRAGMA table_info(' + table_name + ')')
    for info in res:
        header.append(info[1])
    del(header[0])

    print('enter values to add to the table')
    for i in header:
        print(i,': ')
        value = input('value name: ')
        values.append(value)
        
    header = str(header)
    header = header.replace("]","")
    header = header.replace("[","")
    print(header)

    values = str(values)
    values = values.replace("[","")
    values = values.replace("]","")
    print(values)

    data_point = 'INSERT INTO ' + table_name.replace(" ","") + '(' + header + ')' + ' VALUES ' + '(' +values +')'
    print(data_point)
    c.execute(data_point)
    con.commit()

def removefromTable(c, con):
    header=[]
    table_name = input('name of table: ')
    res = c.execute('PRAGMA table_info(' + table_name + ')')
    for info in res:
        header.append(info[1])
    del(header[0])
    print(header)
    catagory = input('enter the heading you want to delete from')
    delete_name_of_data = input('enter the name of the data you want to delete')

    delete_data_point = 'DELETE FROM ' + table_name.replace(" ","") + ' Where ' + catagory + ' = "'+ delete_name_of_data + '"'
    print(delete_data_point)
    c.execute(delete_data_point)
    con.commit()

def updateTable(c, con):
    header=[]
    table_name = input('name of table: ')
    res = c.execute('PRAGMA table_info(' + table_name + ')')
    for info in res:
        header.append(info[1])
    del(header[0])
    print(header)
    catagory = input('enter the heading where you want to update a data point: ')
    update_name_of_data = input('enter the new name of the data point under ' + catagory + ' : ')

    print('for reference: ')
    
    catagory2 = input('enter a name of a heading in the data table: ' + table_name)
    data_point = input('enter the name of the data point under ' + catagory2 + ' : ')

    update_data_point= 'UPDATE ' + table_name + ' SET ' + catagory + '= "' + update_name_of_data + '" WHERE ' + catagory2 + '= "' + data_point + '"'
    print(update_data_point)
    c.execute(update_data_point)
    con.commit()

def viewTable(c, con):
    table_name = input('name of table: ')
    c.execute('SELECT * FROM ' + table_name)
    for record in c.fetchall():
        print(record)
    con.commit()

def Run(c, con):
    ask = input('Create a table : Create / Update the table : Update / Remove data from a table : Remove / Add data to a table : Add / View a Table : View : ')
    if ask == 'Create':
        createTable(c, con)
    elif ask == 'Remove':
        removefromTable(c, con)
    elif ask == 'Add':
        addtoTable(c, con)
    elif ask == 'View':
        viewTable(c, con)
    elif ask == 'Update':
        updateTable(c,con)
    else:
        print('enter create table, remove, add, view')

con, c = database()

while True:
    stay = input('q to exit/s for another action')
    if stay == 's':
        Run(c, con)
    elif stay == 'q':
        dbClose(c)
        break
    else:
        print('enter q or s')


#createTable(c)
#addtoTable(c, con)
#removefromTable(c, con)
#updateTable(c, con)
#viewTable(c, con)




