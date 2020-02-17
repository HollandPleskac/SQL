#sql lesson 5

##Operator                  Description
##=                             Equal
##<>                          Not Equal
##>                             Greater than
##<                             Less than
##>=                           Greater than or equal
##<=                           Less than or equal
##BETWEEN                  Between an inclusive range
##LIKE                         Search for a pattern
##IN                             To specify multiple possible values for a column

import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
#will print student information where the country is USA
##c.execute('SELECT * FROM Students WHERE country="USA"')
##for record in c.fetchall():
##    print(record)

#will print student information where the gpa is greater than or equal 3.0
##c.execute('SELECT * FROM Students WHERE GPA >= 3.0')
##for record in c.fetchall():
##    print(record)

#will print students who took classes before 2015-01-01 from students table 
##c.execute('SELECT * FROM Students WHERE dateStarted <= 2015-01-01')
##for record in c.fetchall():
##    print(record)
    #nobody started before 2015-01-01

#prints out students who live in India and whose city is Bangalore
##c.execute('SELECT * from Students WHERE country="India" and city="Bangalore"')
##for record in c.fetchall():
##    print(record)
#

#prints out students who live in India and whose city is either Bangalore or Delhi
##c.execute('SELECT * from Students WHERE country="India" and city="Bangalore" or city="Delhi"')
##for record in c.fetchall():
##    print(record)

#prints students who don't live in the USA and India
##c.execute('SELECT * from Students WHERE NOT country="India" AND NOT country="USA"')
##for record in c.fetchall():
##    print(record)

#prints students who live in INDia and whose GPA is equal or higher than 3.0
##c.execute('SELECT * from Students WHERE country="India" AND gpa >= "3.0"')
##for record in c.fetchall():
##    print(record)

#prints students who don't live in INDIA and whose gpa is less than or equal to e.0 and started classes before 2017-01-01
##c.execute('SELECT * FROM Students WHERE NOT country="India" AND gpa <= "3.0" AND datestarted <= "2017-01-01"') 
##for record in c.fetchall():
##    print(record)

#prints students who took classes before 2014-01-01 OR after 2018-01-01
c.execute('SELECT * FROM Students WHERE datestarted < "2014-01-01" OR datestarted > "2017-01-01"')
for record in c.fetchall():
    print(record)
conn.commit()
c.close
