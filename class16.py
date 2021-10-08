#has -a Realtionship
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print('Car Name:',self.name)
        print('Car Model:',self.model)
        print('Car color:',self.color)

class Employee:
    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.car=car
    def empinfo(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Car Information....')
        self.car.getinfo()
name=input('Enter car name:')
model=input('Enter car Model:')
color=input('Enter car color:')
car=Car(name,model,color)
emp=Employee(100,'Sunny',car)
emp.empinfo()

