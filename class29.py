#polymorphism
#operator overloading

class Book:
    def __init__(self,pages):
        self.pages=pages 

    def __add__(self,other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)

print(b1+b2)
print()


class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The number of pages:'+str(self.pages)
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)
        return b
b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
print(b1+b2+b3)
print(b1+b2+b3+b4)
print()
#overloading > and<= operator for student class
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self,other):
        return self.marks<=other.marks

s1=Student('Subbu',100)
s2=Student('Ravi',150)
print('s1<s2=',s1<s2)
print('s1>s2=',s1>s2)
print('s1<=s2=',s1<=s2)
print('s1>=s2=',s1>=s2)


#program overload multiplication of employee Objects
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days
class Timesheet(Employee):
    def __init__(self,name,days):
        self.name=name
        self.days=days
    
e=Employee('subbu',1000)
t=Timesheet('subbu',25)
print('Employee salary:',e*t)

print()

#__str__ magic method this method is print object Example
class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
print(b1)# if u print b1 object you can get output:<__main__.Book object at 0x00B18418>
print()
#i dont wont this type of output we are using __str__ methdo <__main__.Book object at 0x00B18418
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The number pages:'+str(self.pages)
b1=Book(100)
print(b1)

