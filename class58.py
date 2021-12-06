#Standard steps to communicate with database:
#1.import thet database specific module
#import cx_Oracle
#import pymysql

#2.Establish Connection between python program and db
#con=cx_Oracle.connect(database information)
#eg:con=cx_oracle.connect('scott/tiger@localhost')

#3.To excute our sql query and to hold result some special object must required that object is Cursor object
#cursor=con.cursor()

#4:excute out sql query
#cursor.excute(sqlquery)---->a single query
#cursor.excutescript(sqlqueries)---> to excute a multiple queries
#cursor.excutemany()-->to excute a parameterized query

#5.Fetch the result:
#cursor.fetch()--->to fetch only one row
#cursor.fetchall()-->to fetch all rows
#cursor.fetchmany(n)--->to fetch n rows

#6.once excute query directly ont update in database
#commit()
#rollback()

#7.con.close()
#cursor.close() 

#working with Oracle database:
#------------------------------
#communication in beetween python and database we should need some softwere driver  that driver name is cx_Oracle
#first install cx_Oracle :pip install


#Example
#1.To connect with oracle dtabase and print version
import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!=None:
    print('connection established sucessfully')
    print('version:',con.version)
else:
    print('connection established not sucessfully')
con.close()

#2.to create employee table in the database
#create table employees(eno number,ename varchar2(10),esar number(2,10) eaddress varchar2(10))
import cx_Oracle
try:
    query="create table employees(eno number(10),ename varchar2(10),esal number(2,10),eaddress varchar2(10))"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print('table dropped sucessfulyy')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('some problem is there')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#3.Drop table
#drop table employee
#4.insert record in to database  excepastly we commit
import cx_Oracle
try:
    query="insert into emplyees (100,'subbu',10000,'hyd')"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print('table dropped sucessfulyy')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('some problem is there')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#insert multiple record:
#excutemany() method
#insert into employess values(:eno,:ename,:esal,:eaddr)
#records=[(200,'sunny',2000,'Ban')
#         (300,'Bummy',3000,'hyd')
#         (400,'chinny',4000'che')]
import cx_Oracle
try:
    query="insert into emplyees values (:eno,:ename,:esal,:eaddr)"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    records=[(200,'sunny',2000,'Ban')
            (300,'Bunny',3000,'hyd')
            (400,'chinny',4000,'che')]
    cursor.executemany(query,records)
    con.commit()
    print('table dropped sucessfulyy')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('some problem is there')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#6.To insert multiple rows with dynamic input from the keyboard
#query="insert into employee(%d,'%s',%f,'%s)"
#cursor.excute(query %(eno,ename,esal,eaddr))
import cx_Oracle
try:
    
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    while True:
        eno=int(input('Enter the Employee Number:'))
        ename=input('Enter Employee Name:')
        esal=float(input('Enter Employee Salary:'))
        eaddr=input('Enter Employee Address:')
        query="insert into employee values(%d,'%s',%f,'%s)"
        cursor.execute(query %(eno,ename,esal,eaddr))
        con.commit()
        print('Record inserted sucessfully')
        option=input('Do you want to insert one more record[yes|No]:')
        if option == 'No':
            break
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('Ther is aproblem')
finally:
    if con:
        con.close()
    if cursor:
        cursor.closr()

#7.By 144 rs whose salary <5000
import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    increment=float(input('Enter Increment Salary:'))
    salrange=float(input('Enter Salary Range:'))
    query= "update employees set esal=esal+%f where esal<%f"
    cursor.execute(query %(increment,salrange)) 
    con.commit()
    print('record updated suceesfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('Ther is aproblem')
finally:
    if con:
        con.close()
    if cursor:
        cursor.closr()

#8.Delete operation:
#-------------------
#delete from employess where esal >5000
import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cutoff=float(input("Enter cutoff  Salary:"))
    query="delete from employee where esal>%f"
    cursor.execute(query %cutoff)
    con.commit()
    print('Record Deleted Suceesfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('there is problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#9.select opertaion:
#------------------
#fetchone()
#fetchall()
#fetchmany()



#fetchone
import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employee"
    cursor.execute(query)
    row=cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('there is problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


#fetchall():
import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employee"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print('Employee Number:',row[0])
        print('Employee Name:',row[1])
        print('Employee Salary:',row[2])
        print('Employe address:',row[3])
        print()
        print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('there is problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


#fetchmany():

import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employee"
    cursor.execute(query)
    n=int(input("Enter the Number of required rows:"))
    data=cursor.fetchmany(n)
    for row in data:
        print('Employee Number:',row[0])
        print('Employee Name:',row[1])
        print('Employee Salary:',row[2])
        print('Employe address:',row[3])
        print()
        print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('there is problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#how to store the data in file
import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employee"
    cursor.execute(query)
    n=int(input("Enter the Number of required rows:"))
    data=cursor.fetchmany(n)
    f=open('dbresult.txt','w')
    f.write(str(data))
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('there is problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()