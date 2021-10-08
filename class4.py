class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print('Hi:',self.name)
        print('your total marks:',self.marks)

    def grade(self):
        if self.marks>=65:
            print('you got first class')
        elif self.marks>=50:
            print('you got second class')
        elif self.marks>=35:
            print('you got third class')
        else:
            print('you are failed')
name=input("enter your name:")
marks=int(input('enter your marks:'))
s=Student(name,marks)
s.display()
s.grade()