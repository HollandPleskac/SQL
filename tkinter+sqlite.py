import sqlite3
from tkinter import *
from tkinter import messagebox


def database():
    dbname=input('connect to a database ')
    conn = sqlite3.connect(dbname+'.db')
    c = conn.cursor
    return c, conn
def dbClose(c):
    c.close()

def Connect(c):
    c.execute('SHOW TABLES')
    for record in c.fetchall():
        print(record)

def window():
    root = Tk()
    root.geometry('300x150')
    label=Label(root, text = 'Connect or Create a Database')
    label1=Label(root, text = 'connect')
    label2=Label(root, text = 'create')
    entry1 = Entry(root)
    entry2 = Entry(root)
    button1 = Button(root, text = 'enter',command=Connect)
    button2 = Button(root, text = 'clear')

    label.grid(row=0,column=1)
    label1.grid(row=1,column=0)
    label2.grid(row=2,column=0)
    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    return root

c, con = database()
root = window()
Connect(c)



dbClose(c)
