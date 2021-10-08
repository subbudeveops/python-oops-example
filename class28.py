#loop whoels
#1.From child class by using super() method we cannot call Parent class instance variable we should use self only
#2.From child class by using super() method we can call Parent class static variable.
class P:
    a=10
    def __init__(self):
        self.b=20
class C(P):
    def m1(self):
        print(super().a)#example of statement 2 example
        #print(super().b)#beacuse first statement example
        print(self.b)#instance variable we can call only with self only

c=C()
c.m1() 

#we can try differnet example by using super() method
class P:
    def __init__(self):
        print('Parent class Constructor')
    def m1(self):
        print('Parent class Inistent method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Paarent Static Method')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
c=C()
#Conclusion:super() method call all method and constructor also

print()
#another Example by using super() method
class P:
    def __init__(self):
        print('Parent class Constructor')
    def m1(self):
        print('Parent class Inistent method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Paarent Static Method')
class C(P):
    def m(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
c=C()
c.m()
#conclusion :from Child class Initance method we can call parent class constuctor and all methos also

print()

#Another Example
class P:
    def __init__(self):
        print('Parent class Constructor')
    def m1(self):
        print('Parent class Inistent method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Paarent Static Method')
class C(P):
    @classmethod
    def m(cls):
        #super().__init__()
        #super().m1()
        super().m2()
        super().m3()
        
c=C()
c.m()
#conclusion:From Child class class method we cannot calling to parent class Constructor and Inistent method only calling parent class Static method and class method
print()
#Another example
class P:
    def __init__(self):
        print('Parent class Constructor')
    def m1(self):
        print('Parent class Inistent method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Paarent Static Method')
class C(P):
    @staticmethod
    def m():
        #super().__init__()
        #super().m1()
        #super().m2()
        #super().m3()
        c.m1()
        c.m2()
        c.m3()
        
c=C()
c.m()
#Conclusion:From child class we cannot call to Parent class members 




