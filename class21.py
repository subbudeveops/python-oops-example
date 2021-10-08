#how to call parent constructor call
#also exmple single inheritance
class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print('Person name:',self.name)
        print('Person IdNumber:',self.idnumber)

class Employee(Person):
    def __init__(self,name,idnumber,esal,post):
        self.esal=esal
        self.post=post
        Person.__init__(self,name,idnumber)
    def empinfo(self):
        emp.display()
        print('Employee Salary:',self.esal)
        print('Employee Post:',self.post)
emp=Employee('subbu',15050,2000,'HR')
emp.empinfo()


print()

#another multi level inheritance
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class Father(Grandfather):
    def __init__(self,grandfathername,fathername):
        Grandfather.__init__(self,grandfathername)
        self.fathername=fathername
class Son(Grandfather):
    def __init__(self,grandfathername,fathername,sonname):
        Father.__init__(self,grandfathername,fathername) 
        self.sonname=sonname
    def display(self):
        print('Grand father Name:',self.grandfathername)
        print('Fathe Name:',self.fathername)
        print('son Name:',self.sonname)
s=Son('Peddasubbareddy','Venkata Subbareddy','chinnasubbareddy')
s.display()


        



