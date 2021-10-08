#inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print('Eat Biriyani and drink beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print('python codeing...')
    def empinfo(self):
        print('Employee Name:',self.name)
        print('Employee age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee salary:',self.esal)
e=Employee('subbu',29,78946,10000)
e.eat()
e.work()
e.empinfo()