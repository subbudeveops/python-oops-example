#inhertence is two types
#1.By composition (has-a Realtionship)
#2.By Inheritance (IS-A Realtionship)
#if we want acess one class method,variable and properties another class
#by using composition(HAS-A Reationship)
class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('Engine specification functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('Car class using Engine functionality')
        print(self.engine.a)
        #or
        print(Engine.a)
        print(self.engine.b)
        self.engine.m1()
c=Car()
c.m2()