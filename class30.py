#method overloading
#if two methods having same name ,but differnt arugument then those metods are said to be overloaded methods
#m1(a)
#m1(a,b)
# if even u can decalre multiple method  it always goes to consider last method only consider
class Test:
    def m1(self):
         print('no-argument')
    def m1(self,a):
        print('singel argument')
    def m1(self,a,b):
        print('double-argument')
t=Test()
t.m1(10,20)
print()
#python not provide method overloading 
#1.Default Argument
#2.variable length argument
#demo of default argument example
class Demo:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('the sum of Three number:',a+b+c)
        elif a!=None and b!=None:
            print('sum of 2 number is:',a+b)
        else:
            print('Pls enter 2 or 3 Arguments')
d=Demo()
d.sum(10,20,30)
d.sum(10,40)
d.sum(10)
print()
#variable length argument
#Demo of Variable length argument
class Demo:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('the sum of:',total)
d=Demo()
d.sum(10)
d.sum(10,20,30,40)
d.sum(10,20,30,40,50)
print()

class Demo:
    def m1(self,*a):
        total=''
        for x in a:
            total=total+x
        print('the sum of:',total)
d=Demo()
d.m1('subbu')
d.m1('subbu','bhavani')
d.m1('subbu','bhavani','lakshmi')
            