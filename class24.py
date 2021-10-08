#hierarchical inheritance
class Parent:
    def func1(self):
        print('This  func1 is in Parent class ')
class Child1(Parent):
    def func2(self):
        print('This func2 is in Child1 class')
class Child2(Parent):
    def func3(self):
        print('this func3 is in child2 class')
c1=Child1()
c2=Child2()
c1.func1()
c1.func2()
c2.func1() 
c2.func3() 
