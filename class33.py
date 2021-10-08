#Constructor overriding
class P:
    def __init__(self):
        print('parent class constructor')
class C(P):
    def __init__(self):
        print('child class constructor')
c=C()
print()
#demo program to call parent class constructor with super() method
class P:
    def __init__(self):
        print('parent class constructor')
class C(P):
    def __init__(self):
        super().__init__()
        print('child class constructor')
c=C()


print()
#another demo program to call parent class constructor with super() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print('Employee Naame:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Emplyee salary:',self.esal)

e1=Employee('subbu',30,101,1000)
e1.display()
e2=Employee('Bhavani',24,102,2000)
e2.display()
