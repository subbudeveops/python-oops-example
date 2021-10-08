#inheritance(IS-A)AND HAS-A exmple
#Car class AND  Employee class Has-A Realtionship because employee just using car functionality not extending
# Peson and Employee IS-A relation ship
#  
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print('\ncar name:{} \ncar model:{} \ncar color:{}'.format(self.name,self.model,self.color))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('Eat Biriyani and drink beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def work(self):
        print('python codeing...')
    def empinfo(self):
        print('Employee Name:',self.name)
        print('Employee age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee salary:',self.esal)
        print('car information.....')
        self.car.getinfo()
car=Car('innova','2.5v','red')
e=Employee('subbu',29,78946,10000,car)
e.eat()
e.work()
e.empinfo()