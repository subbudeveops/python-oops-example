#Abstract class and Abstract methods
from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def display(self):
        pass
class Employee(Person):
    def display(self):
        print('i have one idea')
class Subbu(Person):
    def display(self):
        print('i have two idea')
class Bhavani(Person):
    def display(self):
        print('i have three idea')
e=Employee()
s=Subbu()
b=Bhavani()
e.display()
s.display()
b.display()


print()
class Parent(ABC):
    def m1(self):
        pass
    def m2(self):
        pass
class Child1(Parent):
    def m1(self):
        print('child1 class method')
class Child2(Child1):
    def m2(self):
        print('chilsd2 class method')

c2=Child2()
c2.m1()
c2.m2()

print()
import abc
class P(ABC):
    def s(self):
        print('Abstract Base Class')
class C(P):
    def s(self):
        super().s()
        print('sub class')
c=C()
c.s() 

#example
class A(ABC):
    def __init__(self,value):
        self.value=value
    
    @abstractmethod
    def disp1(self):
        pass
class B(A):
    def disp1(self):
        print(0+self.value)

class mul(A):
    def disp1(self):
        print(0*self.value)
a=B(10)        
m=mul(5)
a.disp1()
m.disp1()












