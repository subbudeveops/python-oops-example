#how to acess object one class to another class

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)

class Test:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()
n=int(input('Enter number of employee:'))
for i in range(n):
    eno=int(input('Enter Employee Number:'))
    ename=input('Enter Employee name:')
    esal=float(input('Enter Employee salayr:'))
    e=Employee(eno,ename,esal)
    Test.modify(e)

    
