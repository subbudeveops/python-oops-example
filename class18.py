#inheritance(IS-A Realtionship)
class P:
    a=10
    def __init__(self):
        print('parent constructor value of b')
        self.b=20
    def m1(self):
        print('parent instance method')
    @classmethod
    def m2(cls):
        print('parent class method')

    @staticmethod
    def m3():
        print('parent static method')

class C(P):
    def __init__(self):
        super().__init__()  #i can call partent class constructor
        self.d=30
c=C()
print(c.a)
print(c.b)
print(c.d)
c.m1()
c.m2()
c.m3()