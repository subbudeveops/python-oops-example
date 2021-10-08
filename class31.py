#Constructor overloading same like method overloading
#constructor overloading not possible in python
#if we define multiple constructor last constructor only consider
class Test:
    def __init__(self):
        print('No-argumert')
    def __init__(self,a):
        print('single-argument')
    def __init__(self,a,b):
        print('two -argument')
t=Test(10,20)
print()
#constructor with default argument
class Test:
    def __init__(self,a=None,b=None,c=None):
        print('constuctor with 0|1|2|3 number of argument')


t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)


print()


#constructor with variable number of length

class Test:
    def __init__(self,*a):
        print('constructor with variable number of length')
t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30)    
