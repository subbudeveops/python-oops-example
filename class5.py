class Student:
    def __init__(self,name,rollno,sub1,sub2,sub3,sub4,sub5,sub6,marks):
        self.name=name
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5
        self.sub6=sub6
        self.marks=marks
    
    def display(self):
        print('Name:',self.name)
        print('Rollno:',self.rollno)
        print('marks of sub1:',self.sub1)
        print('marks of sub2:',self.sub2)
        print('marks of sub3:',self.sub3)
        print('marks of sub4:',self.sub4)
        print('marks of sub5:',self.sub5)
        print('marks of sub6:',self.sub6)
        print('tatal marks:',self.marks)
    def grade(self):
        if self.marks>=65:
            print('you got first class')
        elif self.marks>=50:
            print('you got second class')
        elif self.marks>=35:
            print('you got third class')
        else:
            print('you are failed')
name=input("enter your Name:")
rollno=int(input("enter the rollno:"))
sub1=int(input('enter your sub1:'))
sub2=int(input('enter your sub2:'))
sub3=int(input('enter your sub3:'))
sub4=int(input('enter your sub4:'))
sub5=int(input('enter your sub5:'))
sub6=int(input('enter your sub6:'))
marks=sub1+sub2+sub3+sub4+sub5+sub6
s=Student(name,rollno,sub1,sub2,sub3,sub4,sub5,sub6,marks)
s.display()
s.grade()