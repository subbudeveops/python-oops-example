#public protect and private members 
# how to define public and how to acess public variable
#public variable acess any were
# All the class variable are public
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.engintype=enginetype
c=Car(4,5,'audi')

c.windows=5#here we can over write  values as changes
print(c.windows)#5




#All the class variable are protected
# if you want change proctect variable we cant change in parent class only we can change the child class only
#protect variable acess only subclass or child class

class A:
    def __init__(self,name,age,sal):
        self._name=name
        self._age=age
        self._sal=sal
class B(A):
    def __init__(self,name,age,sal,add):
        super().__init__(name,age,sal)
        self.add=add

a=B('AUDI',30,1000,'sarvayapalli')
print(a._name)
a._name='subbu'#override 
print(a._name)


print()
#private vriable
#private variable we cannot override and wea cannot  acess any where 
# private variable cannot aceed and  cannot modified out side of the class
# Hoe to define
class A:
    def __init__(self,name,age,sal):
        self.__name=name
        self.__age=age
        self.__sal=sal
a=A('subbu',10,1000)  
#print(a.__name)#this is not way of aceesing private vriable
print(a._A__name)#this aceesing private variable
a._A__name='ravi'#this changif of private vriable values
print(a._A__name)
