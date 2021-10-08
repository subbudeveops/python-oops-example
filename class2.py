class Test:
    a=10
    def __init__(Self):
        Test.b=20
    
    @classmethod
    def m1(cls):
        Test.c=30
        cls.d=40
    
    @staticmethod
    def m2():
        Test.e=50
    def m3(Self):
        Test.f=60
t=Test()
Test.m1()
Test.m2()
t.m3()
Test.g=70
print(Test.__dict__)




