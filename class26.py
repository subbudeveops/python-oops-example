#MRO(METHDO RESOLUTION ORDER)
class  D:
    def m1(self):
        print('thid is D class method')

class E:
    def m1(self):
        print('this is E class method')

class F:
    def m1(self):
        print('this is f class method')
class B (D,E):
    def m1(self):
        print('this is b Class method')
class C(D,F):
    def m1(self):
        print('this is C class method')

class A(B,C):
    def m1(self):
        print('this is A class method')
a=A()
a.m1()        