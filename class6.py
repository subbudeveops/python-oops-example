class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

l=[]
n=int(input('Enter Number of Student:'))
for i in range(n):
    
    name=input("Enter the Name:")
    marks=int(input('Enter the marks:'))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    l.append(s)
for s in l:
    print('student Name:',s.getName())
    print('student marks:',s.getMarks())
    print()