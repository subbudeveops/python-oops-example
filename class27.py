#super() method can be used to call  parent class members
#advantage is Code Reusability
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print('Rollno:',self.rollno)
        print('Marks:',self.marks)

class Teacher(Person):
    def __init__(self,name,age,salary,subjects):
        super().__init__(name,age)
        self.salary=salary
        self.subjects=subjects
    def display(self):
        super().display()
        print('Teacher Salary:',self.salary)
        print('Teacher Subject:',self.subjects)

t=Teacher('Bhavani',20,10000,'English')
s=Student('subbu',30,101,95)
t.display()
s.display()
