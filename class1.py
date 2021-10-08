class Student:
    def __init__(self,name,rollno,collage):
        self.name=name
        self.rollno=rollno
        self.collage=collage
    def info(self):
        print('student name:',self.name)
        print('student rollbo:',self.rollno)
        print('studentcollege:',self.collage)
std=[Student('subbu',100,'svrm'),Student('ravi',200,'aits')]
for student in std:
    student.info()