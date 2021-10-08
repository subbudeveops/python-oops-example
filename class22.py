#mlulti level inheritance
class Parent:
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name)
        self.age=age
    def getAge(self):
        return self.age
class Grandchild(Child):
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address=address
    def getAddress(self):
        return self.address

g=Grandchild('subbu',30,'sarvayapalli')
print('Name:{} \nAge:{} \nAddress:{}'.format(g.getName(),g.getAge(),g.getAddress()))


print()

#another multi level inheritance
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class Father(Grandfather):
    def __init__(self,grandfathername,fathername):
        Grandfather.__init__(self,grandfathername)
        self.fathername=fathername
class Son(Grandfather):
    def __init__(self,grandfathername,fathername,sonname):
        Father.__init__(self,grandfathername,fathername) 
        self.sonname=sonname
    def display(self):
        print('Grand father Name:',self.grandfathername)
        print('Fathe Name:',self.fathername)
        print('son Name:',self.sonname)
s=Son('Peddasubbareddy','Venkata Subbareddy','chinnasubbareddy')
s.display()


