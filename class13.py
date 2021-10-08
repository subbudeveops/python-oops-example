#Nested method:method inside method
#purpose: to define method specific repetedly required functionality
class Test:
    def m1(self):
        def cal(a,b):
            print('sum of:',a+b)
            print('division of:',a/b)
            print('multiplication of:',a*b)
            print('difference:',a-b)
            print()
        cal(100,200)
        cal(1000,2000)
t=Test()
t.m1()