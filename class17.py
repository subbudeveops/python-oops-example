#HAS-A Relationship
class X:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('M1 Method of X Class')

class Y:
    c=30
    def __init__(self):
        self.d=40
    def m2(self):
        print('m2 method of Y class')
    def m3(self):
        x=X()
        print(X.a)
        print(x.b)
        x.m1()

        print(self.c)
        print(self.d)
        self.m2()
        print('m3 information of y CLASS')

y=Y()
y.m3()